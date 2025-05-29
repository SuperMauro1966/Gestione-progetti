import mariadb

conn_params = {
    "user": "root",
    "password": "12345678",
    "host": "localhost",
    "database": "gestione_progetti"
}
 
connection = mariadb.connect(**conn_params)

cursor = connection.cursor(dictionary=True)

print("inserire i dati per la creazione della risorsa")



print("Quantita: ")
Quantita = input("-->")

print("Unita di Misura (es. Kg, Litri, Ore, Pezzi): ")
UnitaDiMisura = input("-->")

print("Descrizione Risorse: ")
Descrizione_Risorsa = input("-->")


cursor.execute(
    "INSERT INTO risorsa(Quantita, UnitaDiMisura, Descrizione_Risorsa) VALUES (?, ?, ?)",
    (Quantita, UnitaDiMisura, Descrizione_Risorsa)
)
 
connection.commit()

connection.close()

print("Risorsa inserita con successo!")