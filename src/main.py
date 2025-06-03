import user_interface.WBS
import user_interface.progetto

# menù principale

print("1. progetti")
print("2. WBS")

scelta=input(" scelta --> ")

if scelta == '1':
    user_interface.progetto.menu()
elif scelta == '2':
    user_interface.WBS.menu_wbs()