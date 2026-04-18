import hashlib

# Catálogo completo de brechas de demostración
_DEMO_BREACHES = [
    # ── Redes sociales ────────────────────────────────────────────────────────
    {
        "Name": "Facebook",
        "Domain": "facebook.com",
        "BreachDate": "2019-04-01",
        "PwnCount": 533000000,
        "Description": "En abril de 2019, más de 533 millones de registros de Facebook fueron expuestos, incluyendo números de teléfono, nombres completos, ubicaciones y direcciones de correo.",
        "DataClasses": ["Phone numbers", "Email addresses", "Names", "Geographic locations", "Birthdates"],
        "IsVerified": True,
    },
    {
        "Name": "Instagram",
        "Domain": "instagram.com",
        "BreachDate": "2020-08-21",
        "PwnCount": 49000000,
        "Description": "En 2020, una base de datos mal configurada expuso 49 millones de perfiles de influencers y cuentas comerciales de Instagram.",
        "DataClasses": ["Email addresses", "Phone numbers", "Names", "Usernames", "Geographic locations"],
        "IsVerified": True,
    },
    {
        "Name": "Twitter",
        "Domain": "twitter.com",
        "BreachDate": "2022-07-05",
        "PwnCount": 5400000,
        "Description": "En 2022, una vulnerabilidad en la API de Twitter permitió correlacionar números de teléfono y correos con cuentas de usuarios.",
        "DataClasses": ["Email addresses", "Phone numbers", "Usernames"],
        "IsVerified": True,
    },
    {
        "Name": "LinkedIn",
        "Domain": "linkedin.com",
        "BreachDate": "2021-04-08",
        "PwnCount": 700000000,
        "Description": "En 2021, datos de más de 700 millones de usuarios de LinkedIn fueron raspados y publicados en foros de hackers.",
        "DataClasses": ["Email addresses", "Names", "Phone numbers", "Geographic locations", "Job titles"],
        "IsVerified": True,
    },
    {
        "Name": "Snapchat",
        "Domain": "snapchat.com",
        "BreachDate": "2014-01-01",
        "PwnCount": 4600000,
        "Description": "En enero de 2014, nombres de usuario y números de teléfono de 4.6 millones de cuentas de Snapchat fueron publicados en línea.",
        "DataClasses": ["Usernames", "Phone numbers"],
        "IsVerified": True,
    },
    {
        "Name": "TikTok",
        "Domain": "tiktok.com",
        "BreachDate": "2022-09-05",
        "PwnCount": 1000000000,
        "Description": "En septiembre de 2022, el grupo BlueHornet afirmó haber robado más de 1.000 millones de registros de usuarios de la base de datos interna de TikTok.",
        "DataClasses": ["Email addresses", "Usernames", "Phone numbers", "Birthdates"],
        "IsVerified": False,
    },
    # ── Streaming ─────────────────────────────────────────────────────────────
    {
        "Name": "Netflix",
        "Domain": "netflix.com",
        "BreachDate": "2023-02-14",
        "PwnCount": 1500000,
        "Description": "Credenciales de acceso a cuentas de Netflix fueron encontradas en paquetes de datos filtrados en foros de la dark web.",
        "DataClasses": ["Email addresses", "Passwords", "Usernames"],
        "IsVerified": True,
    },
    {
        "Name": "Spotify",
        "Domain": "spotify.com",
        "BreachDate": "2020-11-01",
        "PwnCount": 350000,
        "Description": "En noviembre de 2020, una base de datos con credenciales de Spotify fue expuesta debido a una mala configuración de un servidor Elasticsearch.",
        "DataClasses": ["Email addresses", "Passwords", "Usernames", "Countries"],
        "IsVerified": True,
    },
    {
        "Name": "Twitch",
        "Domain": "twitch.tv",
        "BreachDate": "2021-10-06",
        "PwnCount": 2800000,
        "Description": "En octubre de 2021, el código fuente de Twitch y datos internos incluyendo información de usuarios fueron filtrados por un actor malicioso anónimo.",
        "DataClasses": ["Email addresses", "Passwords", "Usernames", "Payment info"],
        "IsVerified": True,
    },
    # ── Aplicaciones de uso diario ────────────────────────────────────────────
    {
        "Name": "Adobe",
        "Domain": "adobe.com",
        "BreachDate": "2013-10-04",
        "PwnCount": 152445165,
        "Description": "En octubre de 2013, Adobe sufrió una masiva brecha que expuso 153 millones de registros incluyendo contraseñas cifradas con algoritmo débil.",
        "DataClasses": ["Email addresses", "Password hints", "Passwords", "Usernames"],
        "IsVerified": True,
    },
    {
        "Name": "Canva",
        "Domain": "canva.com",
        "BreachDate": "2019-05-24",
        "PwnCount": 137272116,
        "Description": "En mayo de 2019, Canva sufrió un ataque que expuso 137 millones de cuentas con nombres, correos, ubicaciones y contraseñas cifradas.",
        "DataClasses": ["Email addresses", "Geographic locations", "Names", "Passwords", "Usernames"],
        "IsVerified": True,
    },
    {
        "Name": "Dropbox",
        "Domain": "dropbox.com",
        "BreachDate": "2012-07-01",
        "PwnCount": 68648009,
        "Description": "En 2012, Dropbox confirmó que 68 millones de correos y contraseñas fueron robados y expuestos en 2016.",
        "DataClasses": ["Email addresses", "Passwords"],
        "IsVerified": True,
    },
    {
        "Name": "Duolingo",
        "Domain": "duolingo.com",
        "BreachDate": "2023-01-01",
        "PwnCount": 2600000,
        "Description": "En 2023, datos de 2.6 millones de usuarios de Duolingo fueron raspados mediante una API expuesta y publicados en foros de hacking.",
        "DataClasses": ["Email addresses", "Names", "Usernames", "Languages studied"],
        "IsVerified": True,
    },
    {
        "Name": "Trello",
        "Domain": "trello.com",
        "BreachDate": "2024-01-22",
        "PwnCount": 15115516,
        "Description": "En enero de 2024, una API no autenticada de Trello permitió ligar direcciones de correo con 15 millones de perfiles de usuarios.",
        "DataClasses": ["Email addresses", "Usernames", "Names"],
        "IsVerified": True,
    },
    # ── Plataformas de compras y pagos ─────────────────────────────────────────
    {
        "Name": "eBay",
        "Domain": "ebay.com",
        "BreachDate": "2014-05-21",
        "PwnCount": 145000000,
        "Description": "En 2014, eBay solicitó a sus 145 millones de usuarios que cambiaran sus contraseñas tras una brecha que expuso datos cifrados.",
        "DataClasses": ["Email addresses", "Passwords", "Names", "Physical addresses", "Phone numbers", "Birthdates"],
        "IsVerified": True,
    },
    {
        "Name": "Deezer",
        "Domain": "deezer.com",
        "BreachDate": "2019-01-01",
        "PwnCount": 258000000,
        "Description": "En 2022 se descubrió que datos de 258 millones de usuarios de Deezer fueron robados en 2019 e incluían correos, nombres y fechas de nacimiento.",
        "DataClasses": ["Email addresses", "Names", "Usernames", "Birthdates", "Geographic locations"],
        "IsVerified": True,
    },
    # ── Gaming ────────────────────────────────────────────────────────────────
    {
        "Name": "Steam",
        "Domain": "steampowered.com",
        "BreachDate": "2011-11-10",
        "PwnCount": 35000000,
        "Description": "En noviembre de 2011, los foros de Steam fueron comprometidos exponiendo correos, contraseñas cifradas e información de tarjetas de crédito.",
        "DataClasses": ["Email addresses", "Passwords", "Credit cards", "Personal info"],
        "IsVerified": True,
    },
    {
        "Name": "Riot Games",
        "Domain": "riotgames.com",
        "BreachDate": "2023-01-20",
        "PwnCount": 1000000,
        "Description": "En enero de 2023, Riot Games confirmó que atacantes obtuvieron acceso a su entorno de desarrollo, incluyendo el código fuente de League of Legends y datos de cuentas.",
        "DataClasses": ["Email addresses", "Usernames", "Passwords"],
        "IsVerified": True,
    },
    # ── Educación y trabajo ───────────────────────────────────────────────────
    {
        "Name": "Chegg",
        "Domain": "chegg.com",
        "BreachDate": "2018-09-19",
        "PwnCount": 40000000,
        "Description": "En 2018, la plataforma educativa Chegg sufrió una brecha que expuso 40 millones de registros de estudiantes.",
        "DataClasses": ["Email addresses", "Passwords", "Names", "Birthdates"],
        "IsVerified": True,
    },
    {
        "Name": "Zoom",
        "Domain": "zoom.us",
        "BreachDate": "2020-04-01",
        "PwnCount": 500000,
        "Description": "En 2020, más de 500.000 credenciales de cuentas Zoom fueron encontradas en foros de la dark web y vendidas por precios mínimos.",
        "DataClasses": ["Email addresses", "Passwords", "Meeting URLs", "Host keys"],
        "IsVerified": True,
    },
]

# Índice por categoría para selección determinista variada
_CATEGORIES = {
    "social":    ["Facebook", "Instagram", "Twitter", "LinkedIn", "Snapchat", "TikTok"],
    "streaming": ["Netflix", "Spotify", "Twitch", "Deezer"],
    "apps":      ["Adobe", "Canva", "Dropbox", "Duolingo", "Trello", "Zoom"],
    "shopping":  ["eBay"],
    "gaming":    ["Steam", "Riot Games"],
    "education": ["Chegg"],
}
_BREACH_MAP = {b["Name"]: b for b in _DEMO_BREACHES}


def check_email(email: str) -> list:
    """Devuelve brechas de demostración para el correo indicado."""
    return _demo_breaches_for(email)


def _demo_breaches_for(email: str) -> list:
    """
    Selecciona brechas de demostración de forma determinista según el correo,
    cubriendo al menos una brecha de cada categoría principal.
    """
    digest = int(hashlib.md5(email.lower().encode()).hexdigest(), 16)

    selected = []
    cats = list(_CATEGORIES.values())

    # Toma 1 brecha de cada categoría usando el digest como semilla
    for i, group in enumerate(cats):
        idx = (digest >> (i * 4)) % len(group)
        name = group[idx]
        if name in _BREACH_MAP:
            selected.append(_BREACH_MAP[name])

    # Número total de brechas: entre 3 y 6 dependiendo del correo
    total = 3 + (digest % 4)
    return selected[:total]
