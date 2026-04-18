from flask import Blueprint, render_template, request, redirect, url_for, session
import config

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.get("/health")
def health():
    from flask import jsonify
    return jsonify({"status": "ok", "service": "auth"})


@bp.get("/login")
def login():
    return render_template("login.html")


@bp.post("/login")
def login_post():
    user     = request.form.get("user", "").strip()
    password = request.form.get("password", "")
    if user == config.APP_USER and password == config.APP_PASSWORD:
        session["logged_in"] = True
        return redirect(url_for("dashboard"), 303)
    return render_template("login.html", error="Usuario o contraseña incorrectos")


@bp.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
