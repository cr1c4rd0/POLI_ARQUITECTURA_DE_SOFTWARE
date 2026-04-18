from flask import Blueprint, jsonify, render_template, request, session, redirect, url_for
from services import history_service as hist

bp = Blueprint("history", __name__, url_prefix="/history")


@bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "history"})


@bp.get("/")
def history_page():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    page = int(request.args.get("page", 1))
    data = hist.get_history(page=page)
    return render_template("history.html", **data)


@bp.post("/attend/<int:alert_id>")
def attend(alert_id):
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    hist.mark_attended(alert_id)
    return redirect(url_for("history.history_page"))


@bp.get("/api")
def history_api():
    page = int(request.args.get("page", 1))
    return jsonify(hist.get_history(page=page))
