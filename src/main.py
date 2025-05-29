from db import conn
import progetto

# menù principale

print("1. progetti")

scelta=input(" scelta --> ")

if scelta == 1:
    progetto.menu()