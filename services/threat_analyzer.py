from services import virustotal_service


def analyze(resource_type: str, value: str) -> dict:
    handlers = {
        "url": virustotal_service.scan_url,
        "ip": virustotal_service.scan_ip,
        "domain": virustotal_service.scan_domain,
    }
    handler = handlers.get(resource_type)
    if not handler:
        raise ValueError(f"Tipo de recurso no soportado: {resource_type}")
    result = handler(value)
    result["resource_type"] = resource_type
    result["value"] = value
    return result
