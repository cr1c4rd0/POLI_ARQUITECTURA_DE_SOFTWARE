# Credenciales de acceso (MVP local - usuario quemado)
APP_USER     = "admin"
APP_PASSWORD = "ciberescudo123"

# HIBP - Have I Been Pwned (contraseñas, gratis con k-Anonymity)
HIBP_PASSWORDS_URL = "https://api.pwnedpasswords.com"

REQUEST_TIMEOUT   = 10

# Base de datos local
DATABASE_URI = "sqlite:///ciberescudo.db"

# Registro de servicios (Service Registry - SOA)
SERVICE_REGISTRY = {
    "auth":       {"port": 5001, "health": "/auth/health"},
    "monitoring": {"port": 5002, "health": "/monitoring/health"},
    "passwords":  {"port": 5003, "health": "/passwords/health"},
    "guides":     {"port": 5004, "health": "/guides/health"},
    "history":    {"port": 5005, "health": "/history/health"},
}
