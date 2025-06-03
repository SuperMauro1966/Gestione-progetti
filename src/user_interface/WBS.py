from core.WBS import crea_wbs,\
                    cancella_wbs,\
                    get_all_wbs,\
                    is_wbs_present_by_name,\
                    visualizza_wp

__all__ = [""]

def menu_wbs():
    print("Gestione WBS")
    print("1. Crea WBS")
    print("2. Cancella WBS")
    print("3. Visualizza tutte le WBS")
    print("4. Visualizza i work package")
    print("5. Ritorna al menù principale")
    scelta = input("Scelta --> ")

    if scelta == "1":
        dlg_crea_wbs()
    elif scelta == "2":
        dlg_cancella_wbs()
    elif scelta == "3":
        dlg_visualizza_wbs()
    elif scelta == "4":
        dlg_visualizza_wp()
    elif scelta =="5":
        return
    else:
        print("Scelta non valida, riprova.")

def dlg_crea_wbs():
    print("Creazione nuova WBS")
    while True:
        nome = input("Nome --> ")
        if not is_wbs_present_by_name(nome):
            break
        print("Nome già esistente, scegline un altro.")

    descrizione = input("Descrizione --> ")
    id_progetto = input("ID Progetto --> ")

    crea_wbs(nome, descrizione, id_progetto)

def dlg_cancella_wbs():
    nome = input("Inserisci il nome della WBS da cancellare --> ")
    if is_wbs_present_by_name(nome):
        cancella_wbs(nome)
        print("WBS cancellata.")
    else:
        print("WBS non trovata.")

def dlg_visualizza_wbs():
    risultati = get_all_wbs()
    if risultati:
        print("Elenco delle WBS:")
        for wbs in risultati:
            print(f"- {wbs['Nome']}")
    else:
        print("Nessuna WBS trovata.")


def dlg_visualizza_wp():
    nome = input(" inserisci il nome dei work package della wbs ")
    if is_wbs_present_by_name(nome):
        package = visualizza_wp(nome)
        print("Elenco dei work package")
        for wp in package:
            print(f"- {wp['Nome_WP']} ")
            print(f"- {wp['Descrizione_WP']}")
            print("  ")
    else:
        print("Nessun WP trovato.")
