from db import conn

__all__ = ["menu_risorse", "crea_risorsa"]

def menu_risorse():
    while True:
        print("\n--- Menu Risorse ---")
        print("1. Aggiungi risorsa")
        print("2. Visualizza tutte le risorse")
        print("3. Modifica una risorsa")
        print("4. Cancella una risorsa")
        print("5. Ritorna al menù principale")

        scelta = input("Scelta --> ")

        if scelta == "1":
            crea_risorsa()
        elif scelta == "2":
            visualizza_risorse()
        elif scelta == "3":
            modifica_risorsa()
        elif scelta == "4":
            cancella_risorsa()
        elif scelta == "5":
            break
        else:
            print("Scelta non valida. Riprova.")

def crea_risorsa():
    print("\nInserire i dati per la creazione della risorsa")

    Quantita = input("Quantita: --> ")
    UnitaDiMisura = input("Unita di Misura (es. Kg, Litri, Ore, Pezzi): --> ")
    Descrizione_Risorsa = input("Descrizione Risorsa: --> ")

    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO risorsa(Quantita, UnitaDiMisura, Descrizione_Risorsa) VALUES (?, ?, ?)",
        (quantita, unita, descrizione)
    )
    conn.commit()

    print("Risorsa inserita con successo!")

def visualizza_risorse():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM risorsa")
    risultati = cursor.fetchall()

    print("\n--- Elenco Risorse ---")
    for r in risultati:
        print(f"ID: {r['ID']}, Quantità: {r['Quantita']}, Unità: {r['UnitaDiMisura']}, Descrizione: {r['Descrizione_Risorsa']}")



def cancella_risorsa():
    id_risorsa = input("Inserisci l'ID della risorsa da cancellare: ")

    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM risorsa WHERE ID = ?", (id_risorsa,))
    conn.commit()
    print("Risorsa cancellata con successo!")

def modifica_risorsa():