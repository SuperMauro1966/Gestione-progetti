from core.progetto import is_progetto_present_by_name ,\
                        crea_progetto ,\
                        cancella_progetto ,\
                        get_allproject,\
                        visualizza_dettagli_progetto



__all__ = [""]


def menu():
    while True:
        print("1. crea progetto")
        print("2. cancella progetto")
        print("3. visualizza tutti i progetti")
        print("4. visualizza dettagli di un progetto")
        print("5. ritorno al menù principale")
        scelta = input(" scelta --> ")

        if scelta == "1":
            dlg_crea_progetto()
        elif scelta == "2":
            dlg_cancella_progetto()
        elif scelta == "3":
            dlg_visualizza_progetti()
        elif scelta == "4":
            dlg_visualizza_dettagli_progetto()
        elif scelta == "5":
            return 
        else:
            print("Scelta non valida, riprova.")
    

def dlg_crea_progetto():
    print("inserire i dati per la creazione del progetto")
    presente = True
    while presente:
        print("nome: ")
        nome=input("-->")

        presente = is_progetto_present_by_name(nome)

        if presente :
            print("inserisci un nome diverso")

    print("descrizione: ")
    descrizione=input("-->")
    print("data inizio:")
    data_inizio=input("-->")
    print("data fine: ")
    data_fine=input("-->")

    crea_progetto(nome, descrizione, data_inizio, data_fine)


def dlg_cancella_progetto():
    print("inserisci il nome del progetto da cancellare")
    nome = input(" nome --> ")
    presente = is_progetto_present_by_name(nome)
    if presente:
        cancella_progetto(nome)


def dlg_visualizza_progetti():
    
    risultati= get_allproject()
    
    if risultati:
        print("Elenco dei progetti:")
        for progetto in risultati:
            print(f"- {progetto['Nome']}")
    else:
   
        print("Nessun progetto trovato.")


def dlg_visualizza_dettagli_progetto():
    nome = input("Inserisci il nome del progetto di cui vuoi vedere i dettagli --> ")
    progetto = visualizza_dettagli_progetto(nome)

    if progetto:
        print("\nDettagli del progetto:")
        print(f"Nome        : {progetto['Nome']}")
        print(f"Descrizione : {progetto['Descrizione']}")
        print(f"Data Inizio : {progetto['Data_Inizio']}")
        print(f"Data Fine   : {progetto['Data_Fine']}")
    else:
        print("Progetto non trovato.")

