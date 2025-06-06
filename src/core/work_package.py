from core.db import conn

def crea_wp(nome, descrizione, note, nome_wbs):
    cursor = conn.cursor()
    cursor.execute("SELECT ID_WBS FROM wbs WHERE Nome_WBS = %s ", (nome_wbs,))
    ID = cursor.fetchone()
    ID_WBS = ID[0]
    cursor.execute("""
        INSERT INTO work_package (Nome_WP, Descrizione_WP, Note, ID_WBS_WP)
        VALUES (%s, %s, %s, %s)
    """, (nome, descrizione, note, ID_WBS))
    conn.commit()

def is_wp_present(nome):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) AS nwp FROM work_package WHERE Nome_WP = %s", (nome,))
    result = cursor.fetchone()
    return result['nwp'] > 0

def cancella_wp(nome):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM work_package WHERE Nomw_WP = %s", (nome,))
    conn.commit()

def get_all_wp():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM work_package")
    return cursor.fetchall()

def get_wp(nome):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM work_package WHERE Nomw_WP = %s", (nome,))
    return cursor.fetchone()

def get_tasks_by_wp(nome_wp):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM task WHERE Nome_WP = %s", (nome_wp,))
    return cursor.fetchall()

def get_wbs_by_wp(nome_wp):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT w.* FROM wbs w
        JOIN work_package wp ON wp.Nome_WBS = w.Nome
        WHERE wp.Nomw_WP = %s
    """, (nome_wp,))
    return cursor.fetchone()
