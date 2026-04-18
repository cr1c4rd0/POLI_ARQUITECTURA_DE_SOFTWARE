from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
from services.password_checker import check_password

bp = Blueprint("passwords", __name__, url_prefix="/passwords")


@bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "passwords"})


@bp.get("/check")
def check_form():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("password_check.html")


@bp.post("/check")
def check():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    password = request.form.get("password", "")
    if not password:
        return render_template("password_check.html", error="Ingresa una contraseña.")

    try:
        result = check_password(password)
        return render_template("password_check.html", result=result)
    except Exception as e:
        return render_template("password_check.html", error=f"Error al verificar: {e}")


@bp.post("/api/check")
def check_api():
    """Endpoint REST — la contraseña llega cifrada por HTTPS, nunca se almacena."""
    body = request.get_json(silent=True) or {}
    password = body.get("password", "")
    if not password:
        return jsonify({"error": "Campo 'password' requerido"}), 400
    try:
        return jsonify(check_password(password))
    except Exception as e:
        return jsonify({"error": str(e)}), 502
