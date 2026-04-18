from flask import Flask, render_template, redirect, url_for, session
from routes.auth       import bp as auth_bp
from routes.monitoring import bp as monitoring_bp
from routes.passwords  import bp as passwords_bp
from routes.guides     import bp as guides_bp
from routes.history    import bp as history_bp
from services.history_service import init_db

app = Flask(__name__)
app.secret_key = "ciberescudo-secret-2026"

# Service Registry — registro de blueprints (SOA Facade Pattern)
app.register_blueprint(auth_bp)
app.register_blueprint(monitoring_bp)
app.register_blueprint(passwords_bp)
app.register_blueprint(guides_bp)
app.register_blueprint(history_bp)


@app.get("/")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("dashboard.html")


@app.get("/login")
def login_redirect():
    return redirect(url_for("auth.login"))


@app.get("/api/v1/health")
def health():
    from flask import jsonify
    return jsonify({"status": "ok", "service": "CiberEscudo"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
