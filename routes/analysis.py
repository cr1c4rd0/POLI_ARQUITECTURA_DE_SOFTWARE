from flask import Blueprint, request, jsonify
from services.threat_analyzer import analyze

bp = Blueprint("analysis", __name__, url_prefix="/api/v1")


@bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "CiberEscudo"})


@bp.post("/analyze")
def analyze_resource():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Se requiere body JSON"}), 400

    resource_type = body.get("type")
    value = body.get("value")

    if not resource_type or not value:
        return jsonify({"error": "Campos requeridos: 'type' y 'value'"}), 400

    try:
        result = analyze(resource_type, value)
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error al consultar el servicio de análisis", "detail": str(e)}), 502


@bp.get("/analyze/url")
def analyze_url():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Parámetro 'url' requerido"}), 400
    try:
        return jsonify(analyze("url", url))
    except Exception as e:
        return jsonify({"error": str(e)}), 502


@bp.get("/analyze/ip")
def analyze_ip():
    ip = request.args.get("ip")
    if not ip:
        return jsonify({"error": "Parámetro 'ip' requerido"}), 400
    try:
        return jsonify(analyze("ip", ip))
    except Exception as e:
        return jsonify({"error": str(e)}), 502


@bp.get("/analyze/domain")
def analyze_domain():
    domain = request.args.get("domain")
    if not domain:
        return jsonify({"error": "Parámetro 'domain' requerido"}), 400
    try:
        return jsonify(analyze("domain", domain))
    except Exception as e:
        return jsonify({"error": str(e)}), 502
