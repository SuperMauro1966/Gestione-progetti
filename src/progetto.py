from db import conn

__all__ = ["crea_progetto"]

def menu():
    print("1. crea progetto")
    print("2. cancella progetto")
    print("3. ritorno al menù principale")


def dlg_crea_progetto():
    print("inserire i dati per la creazione del progetto")
    presente = True
    while presente:
        print("nome: ")
        nome=input("-->")

        presente = is_progetto_present_by_name(conn, nome)

        if presente :
            print("inserisci un nome diverso")

    print("descrizione: ")
    descrizione=input("-->")
    print("data inizio:")
    data_inizio=input("-->")
    print("data fine: ")
    data_fine=input("-->")

    crea_progetto(conn,  nome, descrizione, data_inizio, data_fine)

def crea_progetto(conn, nome, desc, di, df):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("INSERT INTO progetto(Nome, Descrizione, Data_Inizio, Data_Fine ) VALUES (?,?,?,?)", (nome, desc, di, df))
    
    conn.commit()

def is_progetto_present_by_name(conn, nome):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS nr FROM progetto WHERE Nome = ?", (nome,))

    result = cursor.fetchone()
    count = result['nr']

    return count > 0




