import os

class Config:
    VIRUSTOTAL_API_KEY = os.environ.get("VIRUSTOTAL_API_KEY", "")
    VIRUSTOTAL_BASE_URL = "https://www.virustotal.com/api/v3"
    REQUEST_TIMEOUT = 10
