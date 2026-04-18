from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
from services import hibp_service
from services import history_service as hist

bp = Blueprint("monitoring", __name__, url_prefix="/monitoring")


def _require_login():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))


@bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "monitoring"})


@bp.get("/check")
def check_form():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("dashboard.html")


@bp.post("/check")
def check_email():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    email = request.form.get("email", "").strip()
    if not email:
        return render_template("dashboard.html", error="Ingresa un correo electrónico.")

    try:
        breaches = hibp_service.check_email(email)
        for b in breaches:
            hist.register_alert(email, b.get("Name", ""), b.get("DataClasses", []))

        return render_template(
            "results.html",
            email=email,
            breaches=breaches,
            total=len(breaches),
        )
    except ValueError as e:
        return render_template("dashboard.html", error=str(e))
    except Exception as e:
        return render_template("dashboard.html", error=f"Error al consultar: {e}")


@bp.get("/breaches/<email>")
def breaches_api(email):
    """Endpoint REST para consulta programática."""
    try:
        data = hibp_service.check_email(email)
        return jsonify({"email": email, "breaches": data, "total": len(data)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 502
