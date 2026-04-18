from flask import Blueprint, jsonify, render_template, session, redirect, url_for
from services.action_guides import get_guide, get_guides_for_breach

bp = Blueprint("guides", __name__, url_prefix="/guides")


@bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "guides"})


@bp.get("/<breach_type>")
def guide(breach_type):
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    g = get_guide(breach_type)
    return render_template("guide_detail.html", guide=g, breach_type=breach_type)


@bp.get("/api/<breach_type>")
def guide_api(breach_type):
    return jsonify(get_guide(breach_type))
