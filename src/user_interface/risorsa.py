from core.risorsa import (
    crea_risorsa,
    get_all_risorse,
    get_risorsa_by_id,
    modifica_risorsa,
    cancella_risorsa,
    get_associazioni_risorse 
)



__all__ = ["menu_risorse"]

def menu_risorse():
    while True:
        print("\n--- Menu Risorse ---")
        print("1. Aggiungi risorsa")
        print("2. Visualizza tutte le risorse")
        print("3. Visualizza associazioni delle risorse") 
        print("4. Modifica una risorsa")
        print("5. Cancella una risorsa")
        print("6. Ritorna al menù principale")

        scelta = input("Scelta --> ")

        if scelta == "1":
            dlg_crea_risorsa()
        elif scelta == "2":
            dlg_visualizza_risorse()
        elif scelta == "3":
            dlg_visualizza_associazioni() 
        elif scelta == "4":
            dlg_modifica_risorsa()
        elif scelta == "5":
            dlg_cancella_risorsa()
        elif scelta == "6":
            break
        else:
            print("Scelta non valida. Riprova.")

def dlg_crea_risorsa():
    print("\nInserire i dati per la creazione della risorsa")
    quantita = input("Quantità: --> ")
    unita = input("Unità di Misura (es. Kg, Litri, Ore, Pezzi): --> ")
    descrizione = input("Descrizione Risorsa: --> ")

    crea_risorsa(quantita, unita, descrizione)
    print("Risorsa inserita con successo!")
    input("\nPremi INVIO per continuare...")

def dlg_visualizza_risorse():
    risorse = get_all_risorse()
    print("\n--- Elenco Risorse ---")
    for r in risorse:
        print(f"ID: {r['ID_Risorsa']}, Quantità: {r['Quantita']}, Unità: {r['UnitaDiMisura']}, Descrizione: {r['Descrizione_Risorsa']}")
    input("\nPremi INVIO per continuare...")


def dlg_modifica_risorsa():
    risorsa_id = input("Inserisci l'ID della risorsa da modificare: ")
    risorsa = get_risorsa_by_id(risorsa_id)

    if risorsa is None:
        print("ID non valido.")
        input("\nPremi INVIO per continuare...")
        return

    print("\nLascia vuoto un campo se non vuoi modificarlo.")

    nuova_quantita = input(f"Nuova Quantità (attuale: {risorsa['Quantita']}): ") or risorsa['Quantita']
    nuova_unita = input(f"Nuova Unità di Misura (attuale: {risorsa['UnitaDiMisura']}): ") or risorsa['UnitaDiMisura']
    nuova_descrizione = input(f"Nuova Descrizione (attuale: {risorsa['Descrizione_Risorsa']}): ") or risorsa['Descrizione_Risorsa']

    modifica_risorsa(risorsa_id, nuova_quantita, nuova_unita, nuova_descrizione)
    print("Risorsa modificata con successo!")
    input("\nPremi INVIO per continuare...")

def dlg_cancella_risorsa():
    risorsa_id = input("Inserisci l'ID della risorsa da cancellare: ")
    cancella_risorsa(risorsa_id)
    print("Risorsa cancellata con successo!")
    input("\nPremi INVIO per continuare...")

  

def dlg_visualizza_associazioni():
    associazioni = get_associazioni_risorse()
    print("\n--- Risorse Associate ai Task ---")
    for a in associazioni:
        print(f"Risorsa: {a['ID_Risorsa']} - {a['Descrizione_Risorsa']}  -->  Task: {a['ID_Task']} - {a['Nome_Task']} ({a['Descrizione_Task']})")
    input("\nPremi INVIO per continuare...")





