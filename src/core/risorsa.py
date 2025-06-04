from core.db import conn

__all__ = [
    "crea_risorsa",
    "get_all_risorse",
    "get_risorsa_by_id",
    "modifica_risorsa",
    "cancella_risorsa"
]

def crea_risorsa(quantita, unita, descrizione):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO risorsa (Quantita, UnitaDiMisura, Descrizione_Risorsa) VALUES (?, ?, ?)",
        (quantita, unita, descrizione)
    )
    conn.commit()

def get_all_risorse():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM risorsa")
    return cursor.fetchall()

def get_risorsa_by_id(risorsa_id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM risorsa WHERE ID_Risorsa = ?", (risorsa_id,))
    return cursor.fetchone()

def modifica_risorsa(risorsa_id, quantita, unita, descrizione):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "UPDATE risorsa SET Quantita = ?, UnitaDiMisura = ?, Descrizione_Risorsa = ? WHERE ID_Risorsa= ?",
        (quantita, unita, descrizione, risorsa_id)
    )
    conn.commit()

def cancella_risorsa(risorsa_id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM risorsa WHERE ID_Risorsa = ?", (risorsa_id,))
    conn.commit()


def get_associazioni_risorse():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT
            r.ID_Risorse
            t.ID_Task,
            t.Nome_Task, t.Descrizione_Task
        FROM
            necessita n
        JOIN
            risorsa r ON n.ID_Risorsa = r.ID_Risorse
        JOIN
            task t ON n.ID_Task = t.ID_Task
        ORDER BY
            r.ID_Risorse, t.ID_Task
    """)
    return cursor.fetchall()
