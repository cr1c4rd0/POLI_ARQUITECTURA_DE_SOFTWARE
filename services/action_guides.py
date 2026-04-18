"""
Servicio de Guías de Acción — genera recomendaciones en español
según el tipo de dato comprometido, con referencias a servicios colombianos.
"""

_GUIDES = {
    "passwords": {
        "title": "Contraseñas comprometidas",
        "icon": "bi-key-fill",
        "color": "danger",
        "steps": [
            "Cambia inmediatamente la contraseña del servicio afectado.",
            "Usa una contraseña única de mínimo 12 caracteres para cada cuenta.",
            "Activa la autenticación de dos factores (2FA) donde sea posible.",
            "Considera usar un gestor de contraseñas (Bitwarden, 1Password).",
            "Revisa si usabas la misma contraseña en otros servicios y cámbiala también.",
        ],
    },
    "email addresses": {
        "title": "Correos electrónicos expuestos",
        "icon": "bi-envelope-exclamation-fill",
        "color": "warning",
        "steps": [
            "Activa alertas de inicio de sesión en tu cuenta de correo.",
            "Revisa las sesiones activas y cierra las que no reconoces.",
            "Activa la verificación en dos pasos en Gmail, Outlook o tu proveedor.",
            "Desconfía de correos que soliciten datos personales o contraseñas.",
        ],
    },
    "credit cards": {
        "title": "Datos financieros comprometidos",
        "icon": "bi-credit-card-2-front-fill",
        "color": "danger",
        "steps": [
            "Contacta a tu banco para bloquear o reemplazar tus tarjetas.",
            "Bancolombia: Línea de atención 24h 01 8000 912 345.",
            "Davivienda: App Daviplata o línea 01 8000 512 000.",
            "Nequi: Reporta desde la app en Ayuda → Reportar problema.",
            "Solicita un extracto y revisa movimientos no reconocidos.",
            "Considera activar notificaciones de compra por SMS/email.",
        ],
    },
    "phone numbers": {
        "title": "Números de teléfono expuestos",
        "icon": "bi-telephone-x-fill",
        "color": "warning",
        "steps": [
            "Contacta a tu operador (Claro, Movistar, Tigo) para verificar tu cuenta.",
            "Solicita protección contra SIM Swapping en tu operador.",
            "Desconfía de mensajes de texto con códigos no solicitados.",
            "Cambia el número de teléfono asociado a cuentas importantes.",
        ],
    },
    "names": {
        "title": "Datos de identidad expuestos",
        "icon": "bi-person-x-fill",
        "color": "warning",
        "steps": [
            "Presenta una queja ante la Superintendencia de Industria y Comercio (SIC).",
            "SIC: www.sic.gov.co — protección de datos personales.",
            "Activa alertas de consulta de tu historial crediticio en Datacrédito.",
            "Revisa tu historial en TransUnion Colombia: www.transunion.co.",
        ],
    },
    "geographic locations": {
        "title": "Ubicación geográfica expuesta",
        "icon": "bi-geo-alt-fill",
        "color": "warning",
        "steps": [
            "Revisa los permisos de ubicación de tus aplicaciones.",
            "Desactiva el historial de ubicación en Google Maps si no lo necesitas.",
            "Considera usar una VPN para ocultar tu ubicación en línea.",
        ],
    },
    "default": {
        "title": "Datos personales expuestos",
        "icon": "bi-shield-exclamation",
        "color": "warning",
        "steps": [
            "Cambia las contraseñas del servicio afectado.",
            "Activa la autenticación de dos factores donde esté disponible.",
            "Monitorea actividad inusual en tus cuentas durante los próximos meses.",
            "Reporta el incidente ante la SIC si consideras que hay daño: www.sic.gov.co.",
        ],
    },
}


def get_guide(data_class: str) -> dict:
    """Retorna la guía de acción para un tipo de dato comprometido."""
    key = data_class.lower()
    return _GUIDES.get(key, _GUIDES["default"])


def get_guides_for_breach(data_classes: list) -> list:
    """Retorna guías únicas y priorizadas para una lista de tipos de datos."""
    seen = set()
    guides = []
    priority = ["passwords", "credit cards", "phone numbers", "names", "email addresses"]
    ordered = [c for c in priority if c in [d.lower() for d in data_classes]]
    ordered += [d for d in data_classes if d.lower() not in priority]

    for data_class in ordered:
        key = data_class.lower()
        if key not in seen:
            seen.add(key)
            guides.append(get_guide(key))
    return guides
