from core.db import conn

__all__ = ["crea_progetto, is_progetto_present_by_name, cancella_progetto, get_allproject, visualizza_dettagli_progetto"]

def crea_progetto(nome, desc, di, df):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("INSERT INTO progetto(Nome_P, Descrizione_P, Data_Inizio, Data_Fine ) VALUES (?,?,?,?)", (nome, desc, di, df))
    
    conn.commit()
    
def is_progetto_present_by_name(nome):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS nr FROM progetto WHERE Nome_P = ?", (nome,))

    result = cursor.fetchone()
    count = result['nr']

    return count > 0

def cancella_progetto(nome):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("DELETE FROM progetto WHERE Nome = ?", (nome,))

    conn.commit()

def get_allproject():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Nome_P, Descrizione_P, Data_Inizio, Data_Fine FROM progetto")
    return cursor.fetchall()
    
def visualizza_dettagli_progetto(nome):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Nome_P, Descrizione_P, Data_Inizio, Data_Fine, Nome_WBS, Descrizione_WBS FROM progetto, wbs WHERE ID_progetto_WBS=ID_progetto AND Nome_P = ?", (nome,))
    return cursor.fetchall()


