from core.milestone import (
    crea_milestone,
    get_all_milestone,
    get_milestone_by_id,
    modifica_milestone,
    cancella_milestone
)

__all__ = ["menu_milestone"]

def menu_milestone():
    while True:
        print("\n--- Menu Milestone ---")
        print("1. Aggiungi milestone")
        print("2. Visualizza tutte le milestone")
        print("3. Modifica una milestone")
        print("4. Cancella una milestone")
        print("5. Torna al menù principale")

        scelta = input("Scelta --> ")

        if scelta == "1":
            dlg_crea_milestone()
        elif scelta == "2":
            dlg_visualizza_milestone()
        elif scelta == "3":
            dlg_modifica_milestone()
        elif scelta == "4":
            dlg_cancella_milestone()
        elif scelta == "5":
            break
        else:
            print("Scelta non valida. Riprova.")

def dlg_crea_milestone():
    print("\nInserisci i dati della nuova milestone")
    nome = input("Nome milestone: ")
    data = input("Data (YYYY-MM-DD): ")

    crea_milestone(nome, data)
    print("Milestone creata con successo!")
    input("\nPremi INVIO per continuare...")

def dlg_visualizza_milestone():
    milestone = get_all_milestone()
    print("\n--- Elenco Milestone ---")
    for m in milestone:
        print(f"ID: {m['ID_Milestone']}, Nome: {m['Nome_Milestone']}, Data: {m['Data_Milestone']}")
    input("\nPremi INVIO per continuare...")

def dlg_modifica_milestone():
    milestone_id = input("Inserisci l'ID della milestone da modificare: ")
    milestone = get_milestone_by_id(milestone_id)

    if milestone is None:
        print("ID non trovato.")
        input("\nPremi INVIO per continuare...")
        return

    nuovo_nome = input(f"Nuovo nome (attuale: {milestone['Nome_Milestone']}): ") or milestone['Nome_Milestone']
    nuova_data = input(f"Nuova data (attuale: {milestone['Data_Milestone']}): ") or milestone['Data_Milestone']

    modifica_milestone(milestone_id, nuovo_nome, nuova_data)
    print("Milestone modificata.")
    input("\nPremi INVIO per continuare...")

def dlg_cancella_milestone():
    milestone_id = input("Inserisci l'ID della milestone da cancellare: ")
    cancella_milestone(milestone_id)
    print("Milestone cancellata.")
    input("\nPremi INVIO per continuare...")
