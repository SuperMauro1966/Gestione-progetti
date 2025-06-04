import user_interface.WBS
import user_interface.progetto
import user_interface.task

def main():
    while True:
        print("\n--- Menu Principale ---")
        print("1. Progetti")
        print("2. WBS")
        print("3. Risorse")
        print("4. task")
        print("5. Esci")


        scelta = input("Scelta --> ")


        if scelta == '1':
            user_interface.progetto.menu()
        elif scelta == '2':
            user_interface.WBS.menu_wbs()
        elif scelta == '3':
            user_interface.risorsa.menu_risorse()
        elif scelta == '4': 
            user_interface.task.menu_task()
        elif scelta == '5':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()

