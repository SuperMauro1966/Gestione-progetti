from db import conn

__all__ = ["crea_progetto"]

def menu():
    print("1. crea progetto")
    print("2. cancella progetto")
    print("3. visualizza tutti i progetti")
    print("4. visualizza dettagli di un progetto")
    print("5. ritorno al menù principale")
    scelta = input(" scelta --> ")



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

def dlg_cancella_progetto():
    print("inserisci il nome del progetto da cancellare")
    nome = input(" nome --> ")
    presente = is_progetto_present_by_name(conn, nome)
    if presente:
        cancella_progetto(conn, nome)



def cancella_progetto(conn, nome):
    cursor = conn.cursor(dictionary=True)

    cursor.execute("DELETE FROM progetto WHERE Nome = ?", (nome,))

    conn.commit()

def dlg_visualizza_progetti(conn):
    raise NotImplementedError



