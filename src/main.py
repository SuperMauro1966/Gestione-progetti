import user_interface.WBS
import user_interface.progetto
import user_interface.task
import user_interface.risorsa
import user_interface.milestone
import user_interface.work_package

def main():
    while True:
        print("\n--- Menu Principale ---")
        print("1. Progetti")
        print("2. WBS")
        print("3. Risorse")
        print("4. task")
        print("5. milestone")
        print("6. work package")
        print("7. Esci")


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
            user_interface.milestone.menu_milestone()
        elif scelta == '6':
            user_interface.work_package.menu_wp()
        elif scelta == '7':
            break
        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()

