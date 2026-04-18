"""
Tests de integración — CiberEscudo
Cubre: auth, dashboard, passwords, history, guides, monitoring (sin API key)
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app as flask_app
from services.history_service import init_db


@pytest.fixture
def client(tmp_path, monkeypatch):
    """Cliente de prueba con DB temporal."""
    db_file = str(tmp_path / "test.db")
    monkeypatch.setattr("services.history_service.DB_PATH", db_file)
    flask_app.config["TESTING"] = True
    flask_app.config["SECRET_KEY"] = "test-secret"
    init_db()
    with flask_app.test_client() as c:
        yield c


@pytest.fixture
def logged_client(client):
    """Cliente ya autenticado."""
    with client.session_transaction() as sess:
        sess["logged_in"] = True
    return client


# ── Auth ──────────────────────────────────────────────────────────────────────

class TestAuth:
    def test_login_page_loads(self, client):
        r = client.get("/auth/login")
        assert r.status_code == 200
        assert b"CiberEscudo" in r.data

    def test_login_redirect_from_root(self, client):
        r = client.get("/", follow_redirects=False)
        assert r.status_code == 302

    def test_login_success(self, client):
        r = client.post("/auth/login",
                        data={"user": "admin", "password": "ciberescudo123"},
                        follow_redirects=True)
        assert r.status_code == 200
        assert b"CiberEscudo" in r.data

    def test_login_wrong_password(self, client):
        r = client.post("/auth/login",
                        data={"user": "admin", "password": "wrongpass"},
                        follow_redirects=True)
        assert r.status_code == 200
        assert "incorrectos".encode() in r.data

    def test_login_wrong_user(self, client):
        r = client.post("/auth/login",
                        data={"user": "hacker", "password": "ciberescudo123"},
                        follow_redirects=True)
        assert r.status_code == 200
        assert "incorrectos".encode() in r.data

    def test_logout(self, logged_client):
        r = logged_client.get("/auth/logout", follow_redirects=True)
        assert r.status_code == 200
        # Después de logout, / debe redirigir a login
        r2 = logged_client.get("/", follow_redirects=False)
        assert r2.status_code == 302

    def test_auth_health(self, client):
        r = client.get("/auth/health")
        assert r.status_code == 200
        assert r.get_json()["status"] == "ok"


# ── Dashboard ─────────────────────────────────────────────────────────────────

class TestDashboard:
    def test_dashboard_requires_login(self, client):
        r = client.get("/")
        assert r.status_code == 302

    def test_dashboard_loads(self, logged_client):
        r = logged_client.get("/")
        assert r.status_code == 200
        assert b"CiberEscudo" in r.data
        assert "correo".encode("utf-8") in r.data

    def test_global_health(self, client):
        r = client.get("/api/v1/health")
        assert r.status_code == 200
        data = r.get_json()
        assert data["status"] == "ok"
        assert data["service"] == "CiberEscudo"


# ── Passwords ─────────────────────────────────────────────────────────────────

class TestPasswords:
    def test_form_requires_login(self, client):
        r = client.get("/passwords/check")
        assert r.status_code == 302

    def test_form_loads(self, logged_client):
        r = logged_client.get("/passwords/check")
        assert r.status_code == 200
        assert "Verificar Contraseña".encode("utf-8") in r.data

    def test_empty_password_shows_error(self, logged_client):
        r = logged_client.post("/passwords/check", data={"password": ""})
        assert r.status_code == 200
        assert "Ingresa".encode("utf-8") in r.data

    def test_known_compromised_password(self, logged_client):
        """'password' es una de las contraseñas más filtradas de HIBP."""
        r = logged_client.post("/passwords/check", data={"password": "password"})
        assert r.status_code == 200
        assert "comprometida".encode("utf-8") in r.data

    def test_strong_unique_password(self, logged_client):
        """Una contraseña aleatoria muy larga no debería estar en HIBP."""
        r = logged_client.post("/passwords/check",
                               data={"password": "zX!9kQ#mP2$vLwR7@nT4"})
        assert r.status_code == 200
        assert "segura".encode("utf-8") in r.data

    def test_api_endpoint_no_body(self, logged_client):
        r = logged_client.post("/passwords/api/check",
                               json={},
                               content_type="application/json")
        assert r.status_code == 400

    def test_api_endpoint_with_password(self, logged_client):
        r = logged_client.post("/passwords/api/check",
                               json={"password": "password123"},
                               content_type="application/json")
        assert r.status_code == 200
        data = r.get_json()
        assert "compromised" in data
        assert "count" in data

    def test_passwords_health(self, client):
        r = client.get("/passwords/health")
        assert r.status_code == 200
        assert r.get_json()["status"] == "ok"


# ── History ───────────────────────────────────────────────────────────────────

class TestHistory:
    def test_history_requires_login(self, client):
        r = client.get("/history/")
        assert r.status_code == 302

    def test_history_empty(self, logged_client):
        r = logged_client.get("/history/")
        assert r.status_code == 200
        assert "Historial".encode("utf-8") in r.data

    def test_history_shows_alerts(self, logged_client):
        from services import history_service as hist
        hist.register_alert("victim@example.com", "TestBreach", ["Passwords", "Emails"])
        r = logged_client.get("/history/")
        assert r.status_code == 200
        assert b"TestBreach" in r.data

    def test_attend_alert(self, logged_client):
        from services import history_service as hist
        hist.register_alert("victim@example.com", "AnotherBreach", ["Phones"])
        data = hist.get_history()
        alert_id = data["alerts"][0]["id"]
        r = logged_client.post(f"/history/attend/{alert_id}", follow_redirects=True)
        assert r.status_code == 200
        updated = hist.get_history()
        assert updated["alerts"][0]["status"] == "ATENDIDA"

    def test_history_api(self, client):
        r = client.get("/history/api")
        assert r.status_code == 200
        data = r.get_json()
        assert "alerts" in data
        assert "total" in data

    def test_history_health(self, client):
        r = client.get("/history/health")
        assert r.status_code == 200
        assert r.get_json()["status"] == "ok"


# ── Guides ────────────────────────────────────────────────────────────────────

class TestGuides:
    def test_guide_requires_login(self, client):
        r = client.get("/guides/passwords")
        assert r.status_code == 302

    @pytest.mark.parametrize("breach_type", [
        "passwords", "email addresses", "credit cards",
        "phone numbers", "names", "geographic locations", "unknown-type"
    ])
    def test_guide_loads(self, logged_client, breach_type):
        r = logged_client.get(f"/guides/{breach_type}")
        assert r.status_code == 200
        assert "Guía".encode("utf-8") in r.data

    def test_guide_api(self, client):
        r = client.get("/guides/api/passwords")
        assert r.status_code == 200
        data = r.get_json()
        assert "title" in data
        assert "steps" in data

    def test_guide_api_default_fallback(self, client):
        r = client.get("/guides/api/nonexistent-data-type")
        assert r.status_code == 200
        data = r.get_json()
        assert "steps" in data

    def test_guides_health(self, client):
        r = client.get("/guides/health")
        assert r.status_code == 200
        assert r.get_json()["status"] == "ok"


# ── Monitoring ────────────────────────────────────────────────────────────────

class TestMonitoring:
    def test_monitoring_requires_login(self, client):
        r = client.post("/monitoring/check", data={"email": "x@x.com"})
        assert r.status_code == 302

    def test_empty_email_shows_error(self, logged_client):
        r = logged_client.post("/monitoring/check", data={"email": ""})
        assert r.status_code == 200
        assert "Ingresa".encode("utf-8") in r.data

    def test_demo_mode_returns_breaches(self, logged_client):
        r = logged_client.post("/monitoring/check",
                               data={"email": "test@gmail.com"})
        assert r.status_code == 200
        assert "filtración".encode("utf-8") in r.data or "PWNED".encode() in r.data

    def test_monitoring_health(self, client):
        r = client.get("/monitoring/health")
        assert r.status_code == 200
        assert r.get_json()["status"] == "ok"


# ── Password checker service unit tests ──────────────────────────────────────

class TestPasswordCheckerService:
    def test_check_password_returns_dict(self):
        from services.password_checker import check_password
        result = check_password("test")
        assert isinstance(result, dict)
        assert "compromised" in result
        assert "count" in result
        assert "message" in result

    def test_very_common_password_is_compromised(self):
        from services.password_checker import check_password
        result = check_password("123456")
        assert result["compromised"] is True
        assert result["count"] > 0

    def test_k_anonymity_only_sends_prefix(self, monkeypatch):
        """Verifica que solo se envía el prefijo de 5 chars del hash SHA-1."""
        import hashlib
        import services.password_checker as pc
        calls = []
        original_get = __import__("requests").get

        def mock_get(url, **kwargs):
            calls.append(url)
            return original_get(url, **kwargs)

        monkeypatch.setattr("requests.get", mock_get)
        pc.check_password("mypassword")
        assert len(calls) == 1
        sha1 = hashlib.sha1("mypassword".encode()).hexdigest().upper()
        assert sha1[:5] in calls[0]
        assert sha1[5:] not in calls[0]


# ── History service unit tests ────────────────────────────────────────────────

class TestHistoryService:
    def test_register_and_retrieve(self, monkeypatch, tmp_path):
        db = str(tmp_path / "h.db")
        monkeypatch.setattr("services.history_service.DB_PATH", db)
        from services import history_service as hist
        hist.init_db()
        hist.register_alert("a@b.com", "Breach1", ["Passwords"])
        data = hist.get_history()
        assert data["total"] == 1
        assert data["alerts"][0]["email"] == "a@b.com"

    def test_no_duplicate_alerts(self, monkeypatch, tmp_path):
        db = str(tmp_path / "h2.db")
        monkeypatch.setattr("services.history_service.DB_PATH", db)
        from services import history_service as hist
        hist.init_db()
        hist.register_alert("a@b.com", "Breach1", ["Passwords"])
        hist.register_alert("a@b.com", "Breach1", ["Passwords"])
        data = hist.get_history()
        assert data["total"] == 1

    def test_pagination(self, monkeypatch, tmp_path):
        db = str(tmp_path / "h3.db")
        monkeypatch.setattr("services.history_service.DB_PATH", db)
        from services import history_service as hist
        hist.init_db()
        for i in range(25):
            hist.register_alert(f"u{i}@b.com", f"Breach{i}", ["Names"])
        data = hist.get_history(page=1, per_page=20)
        assert len(data["alerts"]) == 20
        assert data["pages"] == 2

    def test_mark_attended(self, monkeypatch, tmp_path):
        db = str(tmp_path / "h4.db")
        monkeypatch.setattr("services.history_service.DB_PATH", db)
        from services import history_service as hist
        hist.init_db()
        hist.register_alert("x@x.com", "BreachX", ["Emails"])
        alert_id = hist.get_history()["alerts"][0]["id"]
        hist.mark_attended(alert_id)
        status = hist.get_history()["alerts"][0]["status"]
        assert status == "ATENDIDA"
