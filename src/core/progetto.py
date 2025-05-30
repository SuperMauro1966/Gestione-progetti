from core.db import conn

__all__ = ["crea_progetto"]

def crea_progetto(nome, desc, di, df):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("INSERT INTO progetto(Nome, Descrizione, Data_Inizio, Data_Fine ) VALUES (?,?,?,?)", (nome, desc, di, df))
    
    conn.commit()
    
def is_progetto_present_by_name(nome):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS nr FROM progetto WHERE Nome = ?", (nome,))

    result = cursor.fetchone()
    count = result['nr']

    return count > 0

def cancella_progetto(nome):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("DELETE FROM progetto WHERE Nome = ?", (nome,))

    conn.commit()


    


