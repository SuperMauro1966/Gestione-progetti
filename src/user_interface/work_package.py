from core.work_package import crea_wp, is_wp_present, cancella_wp, get_all_wp, get_wp, get_tasks_by_wp, get_wbs_by_wp

def menu_wp():
    while True:
        print("\n--- Menu Work Package ---")
        print("1. crea work package")
        print("2. cancella work package")
        print("3. visualizza tutti i work package")
        print("4. visualizza in dettaglio un work package")
        print("5. visualizza i task associati al work package")
        print("6. visualizza wbs associata")
        print("7. Esci")

        scelta = input("scelta --> ")

        if scelta == '1':
            dlg_crea_wp()
        elif scelta == '2':
            dlg_cancella_wp()
        elif scelta == '3':
            dlg_visualizza_wp()
        elif scelta == '4':
            dlg_visualizza_un_wp()
        elif scelta == '5':
            dlg_task_wp()
        elif scelta == '6':
            dlg_wbs_wp()
        elif scelta == '7':
            return
        else:
            print("scelta non valida")

def dlg_crea_wp(): 
    while True:
        nome = input("Nome --> ")
        if not is_wp_present(nome):
            break
        print("Nome già presente, inserisci un nome diverso.")

    descrizione = input("Descrizione --> ")
    note = input("Note personali --> ")
    nome_wbs = input("Nome della WBS a cui è associata --> ")

    crea_wp(nome, descrizione, note, nome_wbs)
    print("Work package creato con successo.")

def dlg_cancella_wp():
    nome = input("Nome del work package da cancellare --> ")
    if not is_wp_present(nome):
        print("Work package non trovato.")
        return
    cancella_wp(nome)
    print("Work package cancellato con successo.")

def dlg_visualizza_wp():
    wps = get_all_wp()
    if not wps:
        print("Nessun work package presente.")
        return
    for wp in wps:
        print(f"- {wp['Nomw_WP']}: {wp['Descrizione']}")

def dlg_visualizza_un_wp():
    nome = input("Nome del work package --> ")
    wp = get_wp(nome)
    if wp:
        print(f"Nome: {wp['Nomw_WP']}")
        print(f"Descrizione: {wp['Descrizione']}")
        print(f"Note: {wp['Note']}")
        print(f"WBS associata: {wp['Nome_WBS']}")
    else:
        print("Work package non trovato.")

def dlg_task_wp():
    nome = input("Nome del work package --> ")
    tasks = get_tasks_by_wp(nome)
    if tasks:
        print(f"Task associati a '{nome}':")
        for task in tasks:
            print(f"- {task['Nome']}: {task['Descrizione']}")
    else:
        print("Nessun task associato o WP inesistente.")

def dlg_wbs_wp():
    nome = input("Nome del work package --> ")
    wbs = get_wbs_by_wp(nome)
    if wbs:
        print(f"WBS associata a '{nome}':")
        print(f"- Nome: {wbs['Nome']}")
        print(f"- Descrizione: {wbs['Descrizione']}")
    else:
        print("WBS non trovata o WP inesistente.")
