import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "ciberescudo.db")


def _conn():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    with _conn() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS alerts (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                email     TEXT    NOT NULL,
                breach    TEXT    NOT NULL,
                data_cls  TEXT    NOT NULL,
                date_det  TEXT    NOT NULL,
                status    TEXT    NOT NULL DEFAULT 'PENDIENTE'
            )
        """)


def register_alert(email: str, breach_name: str, data_classes: list):
    with _conn() as con:
        exists = con.execute(
            "SELECT 1 FROM alerts WHERE email=? AND breach=?", (email, breach_name)
        ).fetchone()
        if not exists:
            con.execute(
                "INSERT INTO alerts (email, breach, data_cls, date_det) VALUES (?,?,?,?)",
                (email, breach_name, ", ".join(data_classes), datetime.now().strftime("%Y-%m-%d %H:%M")),
            )


def get_history(page: int = 1, per_page: int = 20) -> dict:
    offset = (page - 1) * per_page
    with _conn() as con:
        total = con.execute("SELECT COUNT(*) FROM alerts").fetchone()[0]
        rows = con.execute(
            "SELECT * FROM alerts ORDER BY id DESC LIMIT ? OFFSET ?",
            (per_page, offset),
        ).fetchall()
    return {
        "alerts": [dict(r) for r in rows],
        "total": total,
        "page": page,
        "pages": max(1, (total + per_page - 1) // per_page),
    }


def mark_attended(alert_id: int):
    with _conn() as con:
        con.execute("UPDATE alerts SET status='ATENDIDA' WHERE id=?", (alert_id,))
