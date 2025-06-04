from core.db import conn

__all__ = ["crea_wbs", "is_wbs_present_by_name", "cancella_wbs", "get_all_wbs", "visualizza_wp"]

def crea_wbs(nome, descrizione, id_progetto):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO WBS (Nome, Descrizione, ID_WBS) VALUES (?, ?, ?)",
        (nome, descrizione, id_progetto)
    )
    conn.commit()

def is_wbs_present_by_name(nome):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT COUNT(*) AS nr FROM WBS WHERE Nome = ?", (nome,)
    )
    result = cursor.fetchone()
    return result["nr"] > 0

def cancella_wbs(nome):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM WBS WHERE Nome = ?", (nome,))
    conn.commit()

def get_all_wbs():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM WBS")
    return cursor.fetchall()

def visualizza_wp(nome):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT Nome_WP, Descrizione_WP FROM work_package, WBS WHERE ID_WBS = ID_WBS AND Nome = ?", (nome,)
    )
    return cursor.fetchall()