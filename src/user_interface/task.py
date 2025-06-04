from core.task import crea_task,\
                       individua_task,\
                       cancella_task,\
                       get_alltask,\
                       get_onetask,\
                       visualizza_task_wp

def menu_task():
    print("1 creazione task")
    print("2. cancellazione task finita")
    print("3. cancellazione task non finita")
    print("4. visualizza tutte le task")
    print("5. visualizzare una task specifica")
    print("6. visualizza task di un work package")
    print("7. ritorna al menù principale")

    scelta = input(" scelta --> ")

    if scelta == 1:
        dlg_crea_task()
    elif scelta == 2:
        dlg_cancella_task_finita()
    elif scelta == 3:
        dlg_cancella_task_non_finita()
    elif scelta == 4:
        dlg_visualizza_task()
    elif scelta == 5:
        dlg_visualizza_task_specifica()
    elif scelta == 6:
        dlg_visualizza_task_wp()
    elif scelta == 7:
        return
    else:
        print("scelta non valida")

def dlg_crea_task():
    print("inserisci i dati da inserire")
    print("Nome:")
    nome = input(" --> ")
    print("Descrizione: ")
    descrizione = input(" --> ")
    
    crea_task(nome, descrizione)

def dlg_cancella_task_finita():
    nome = input(" inserisci il nome della task già finita da cancellare --> ")
    presente = individua_task(nome)
    if presente:
        cancella_task(nome)


def dlg_cancella_task_non_finita():
    nome = input(" inserisci il nome della task non finita da cancellare --> ")
    presente = individua_task(nome)
    if presente:
        cancella_task(nome)

def dlg_visualizza_task():
    tasks=get_alltask()
    if tasks:
        for task in tasks:
            print(f"- {task['Nome_Task']}")

def dlg_visualizza_task_specifica():
    nome = input(" inserisci il nome della task --> ")
    task = get_onetask(nome)
    if task:
        print("nome: ")
        print(f"- {task['Nome_Task']}")
        print("descrizione: ")
        print(f"- {task['Descrizione_Task']}")
    else:
        print("task non esistente")


def dlg_visualizza_task_wp():
    nome = input("insserisci il nome del work package")
    tasks = visualizza_task_wp(nome)
    if tasks:
        for task in tasks:
            print(f"- {task['Nome_Task']}")
        else:
            print("questo work package non esiste")