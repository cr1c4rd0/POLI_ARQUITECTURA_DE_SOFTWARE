from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from routes.analysis import bp as analysis_bp
from services.threat_analyzer import analyze

app = Flask(__name__)
app.secret_key = "ciberescudo-secret-2026"

USUARIO = "admin"
PASSWORD = "ciberescudo123"


@app.get("/")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("dashboard.html")


@app.get("/login")
def login():
    return render_template("login.html")


@app.post("/login")
def login_post():
    email = request.form.get("user", "").strip()
    password = request.form.get("password", "")
    if email == USUARIO and password == PASSWORD:
        session["logged_in"] = True
        return redirect(url_for("dashboard"))
    return render_template("login.html", error="Usuario o contraseña incorrectos")


@app.get("/results")
def results():
    resource_type = request.args.get("type", "url")
    value = request.args.get("value", "").strip()
    now = datetime.now().strftime("%d %b %Y, %H:%M")

    if not value:
        return redirect(url_for("dashboard"))

    try:
        data = analyze(resource_type, value)
        engines = _build_engines(data)
        return render_template(
            "results.html",
            result=data,
            engines=engines,
            resource_type=resource_type,
            now=now,
        )
    except Exception as e:
        return render_template(
            "results.html",
            result=None,
            engines=[],
            resource_type=resource_type,
            error=str(e),
            now=now,
        )


def _build_engines(data: dict) -> list:
    raw = data.get("_engines") or {}
    if not raw:
        return []
    engines = []
    for name, info in raw.items():
        engines.append({
            "name": name,
            "result": info.get("result"),
            "category": info.get("category", "undetected"),
        })
    return sorted(engines, key=lambda e: (e["category"] != "malicious", e["category"] != "suspicious"))


if __name__ == "__main__":
    app.run(debug=True)
