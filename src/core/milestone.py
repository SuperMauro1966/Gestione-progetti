from core.db import conn

__all__ = [
    "crea_milestone",
    "get_all_milestone",
    "get_milestone_by_id",
    "modifica_milestone",
    "cancella_milestone"
]

def crea_milestone(nome, data):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO milestone (Nome_Milestone, Data) VALUES (?, ?)",
        (nome, data)
    )
    conn.commit()

def get_all_milestone():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM milestone")
    return cursor.fetchall()

def get_milestone_by_id(milestone_id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM milestone WHERE ID_Milestone = ?", (milestone_id,))
    return cursor.fetchone()

def modifica_milestone(milestone_id, nuovo_nome, nuova_data):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "UPDATE milestone SET Nome_Milestone = ?, Data = ? WHERE ID_Milestone = ?",
        (nuovo_nome, nuova_data, milestone_id)
    )
    conn.commit()

def cancella_milestone(milestone_id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM milestone WHERE ID_Milestone = ?", (milestone_id,))
    conn.commit()
