import hashlib
import requests
import config


def check_password(password: str) -> dict:
    """
    Verifica si una contraseña fue expuesta usando el modelo k-Anonymity.
    La contraseña nunca sale del servidor — solo se envían los primeros 5
    caracteres del hash SHA-1.
    """
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    resp = requests.get(
        f"{config.HIBP_PASSWORDS_URL}/range/{prefix}",
        timeout=config.REQUEST_TIMEOUT,
    )
    resp.raise_for_status()

    count = 0
    for line in resp.text.splitlines():
        hash_suffix, times = line.split(":")
        if hash_suffix == suffix:
            count = int(times)
            break

    return {
        "compromised": count > 0,
        "count": count,
        "message": (
            f"Esta contraseña apareció {count:,} veces en filtraciones conocidas."
            if count > 0
            else "Esta contraseña no aparece en filtraciones conocidas. ✓"
        ),
    }
