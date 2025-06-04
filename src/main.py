import user_interface.WBS
import user_interface.progetto
import user_interface.task

# menù principale

print("1. progetti")
print("2. WBS")
print("3. task")

scelta=input(" scelta --> ")

if scelta == '1':
    user_interface.progetto.menu()
elif scelta == '2':
    user_interface.WBS.menu_wbs()
elif scelta == '3':
    user_interface.task.menu_task()