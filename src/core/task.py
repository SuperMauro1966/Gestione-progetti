from core.db import conn

__all__=["crea_task, individua_task, cancella_task, get_alltask, get_onetask"]

def crea_task(nome, descrizione):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("INSERT INTO task (Nome_Task, Descrizione_Task) VALUES(?,?)", (nome, descrizione))

    conn.commit()


def individua_task(nome):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS nd FROM task WHERE Nome_Task = ?", (nome))

    result = cursor.fetchone()
    count=result['nd']

    return count

def cancella_task(nome):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("DELETE FROM progetto WHERE Nome = ?", (nome,))

    conn.commit()

def get_alltask():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Nome_Task FROM task")
    return cursor.fetchall()

def get_onetask(nome):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Nome_Task, Descrizione_Task FROM task WHERE Nome_Task = ?", (nome))
    return cursor.fetchone()

def visualizza_task_wp(nome)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Nome_Task, Descrizione_Task FROM task, work package")
