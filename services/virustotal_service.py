import base64
import requests
from config import Config


def _headers():
    return {"x-apikey": Config.VIRUSTOTAL_API_KEY}


def scan_url(url: str) -> dict:
    encoded = base64.urlsafe_b64encode(url.encode()).rstrip(b"=").decode()
    resp = requests.get(
        f"{Config.VIRUSTOTAL_BASE_URL}/urls/{encoded}",
        headers=_headers(),
        timeout=Config.REQUEST_TIMEOUT,
    )
    if resp.status_code == 404:
        submit = requests.post(
            f"{Config.VIRUSTOTAL_BASE_URL}/urls",
            headers=_headers(),
            data={"url": url},
            timeout=Config.REQUEST_TIMEOUT,
        )
        submit.raise_for_status()
        return {"status": "queued", "message": "URL submitted for analysis"}
    resp.raise_for_status()
    return _parse_url_result(resp.json())


def scan_ip(ip: str) -> dict:
    resp = requests.get(
        f"{Config.VIRUSTOTAL_BASE_URL}/ip_addresses/{ip}",
        headers=_headers(),
        timeout=Config.REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    return _parse_ip_result(resp.json())


def scan_domain(domain: str) -> dict:
    resp = requests.get(
        f"{Config.VIRUSTOTAL_BASE_URL}/domains/{domain}",
        headers=_headers(),
        timeout=Config.REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    return _parse_domain_result(resp.json())


def _parse_url_result(data: dict) -> dict:
    attrs = data.get("data", {}).get("attributes", {})
    stats = attrs.get("last_analysis_stats", {})
    return {
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "harmless": stats.get("harmless", 0),
        "undetected": stats.get("undetected", 0),
        "verdict": _verdict(stats),
        "_engines": attrs.get("last_analysis_results", {}),
    }


def _parse_ip_result(data: dict) -> dict:
    attrs = data.get("data", {}).get("attributes", {})
    stats = attrs.get("last_analysis_stats", {})
    return {
        "country": attrs.get("country", "unknown"),
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "harmless": stats.get("harmless", 0),
        "undetected": stats.get("undetected", 0),
        "verdict": _verdict(stats),
        "_engines": attrs.get("last_analysis_results", {}),
    }


def _parse_domain_result(data: dict) -> dict:
    attrs = data.get("data", {}).get("attributes", {})
    stats = attrs.get("last_analysis_stats", {})
    return {
        "registrar": attrs.get("registrar", "unknown"),
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "harmless": stats.get("harmless", 0),
        "undetected": stats.get("undetected", 0),
        "verdict": _verdict(stats),
        "_engines": attrs.get("last_analysis_results", {}),
    }


def _verdict(stats: dict) -> str:
    if stats.get("malicious", 0) > 0:
        return "malicious"
    if stats.get("suspicious", 0) > 0:
        return "suspicious"
    return "clean"
