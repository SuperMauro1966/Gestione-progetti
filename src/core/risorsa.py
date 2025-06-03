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
        (Quantita, UnitaDiMisura, Descrizione_Risorsa)
    )
    conn.commit()
    print("Risorsa inserita con successo!")
    torna_al_menu()

def visualizza_risorse():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM risorsa")
    risultati = cursor.fetchall()
    print("\n--- Elenco Risorse ---")
    for r in risultati:
        print(f"ID: {r['ID']}, Quantità: {r['Quantita']}, Unità: {r['UnitaDiMisura']}, Descrizione: {r['Descrizione_Risorsa']}")
    torna_al_menu()

def cancella_risorsa():
    id_risorsa = input("Inserisci l'ID della risorsa da cancellare: ")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM risorsa WHERE ID = ?", (id_risorsa,))
    conn.commit()
    print("Risorsa cancellata con successo!")
    torna_al_menu()

def modifica_risorsa():
    id_risorsa = input("Inserisci l'ID della risorsa da modificare: ")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM risorsa WHERE ID = ?", (id_risorsa,))
    risorsa = cursor.fetchone()

    if risorsa is None:
        print("ID non valido.")
        torna_al_menu()
        return

    print("\nLascia vuoto un campo se non vuoi modificarlo.")

    nuova_quantita = input(f"Nuova Quantità (attuale: {risorsa['Quantita']}): ")
    if nuova_quantita == "":
        nuova_quantita = risorsa['Quantita']

    nuova_unita = input(f"Nuova Unità di Misura (attuale: {risorsa['UnitaDiMisura']}): ")
    if nuova_unita == "":
        nuova_unita = risorsa['UnitaDiMisura']

    nuova_descrizione = input(f"Nuova Descrizione (attuale: {risorsa['Descrizione_Risorsa']}): ")
    if nuova_descrizione == "":
        nuova_descrizione = risorsa['Descrizione_Risorsa']

    cursor.execute(
        "UPDATE risorsa SET Quantita = ?, UnitaDiMisura = ?, Descrizione_Risorsa = ? WHERE ID = ?",
        (nuova_quantita, nuova_unita, nuova_descrizione, id_risorsa)
    )
    conn.commit()
    print("Risorsa modificata con successo!")
    torna_al_menu()

def torna_al_menu():
    input("\nPremi INVIO per tornare al menu risorse...")

if __name__ == "__main__":
    menu_risorse()
