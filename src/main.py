import user_interface.WBS
import user_interface.risorsa
import user_interface.task
import user_interface.milestone
import user_interface.work_package
import user_interface.progetto

def main():
    try:
        while True:
            print("\n--- Menu Principale ---")
            print("1. Progetti")
            print("2. WBS")
            print("3. Risorse")
            print("4. Task")
            print("5. Milestone")
            print("6. Work Package")
            print("Premi CTRL-C per uscire")

            scelta = input("Scelta --> ")

            match scelta:
                case '1':
                    user_interface.progetto.menu()
                case '2':
                    user_interface.WBS.menu_wbs()
                case '3':
                    user_interface.risorsa.menu_risorse()
                case '4':
                    user_interface.task.menu_task()
                case '5':
                    user_interface.milestone.menu_milestone()
                case '6':
                    user_interface.work_package.menu_wp()
                case _:
                    print("Scelta non valida, riprova.")
    except KeyboardInterrupt:
        print("\nUscita dal programma...")
        return




if __name__ == "__main__":
    main()

"""def main():
    while True:
            print("\n--- Menu Principale ---")
            print("1. Progetti")
            print("2. WBS")
            print("3. Risorse")
            print("4. Task")
            print("5. Milestone")
            print("6. Work Package")
            print("Premi CTRL-C per uscire")

            scelta = input("Scelta --> ")

            match scelta:
                case '1':
                    user_interface.progetto.menu()
                case '2':
                    user_interface.WBS.menu_wbs()
                case '3':
                    user_interface.risorsa.menu_risorse()
                case '4':
                    user_interface.task.menu_task()
                case '5':
                    user_interface.milestone.menu_milestone()
                case '6':
                    user_interface.work_package.menu_wp()
                case _:
                    print("Scelta non valida, riprova.")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("Esecuzione Interrotta")"""


