import mariadb

conn_params = {
    "user": "root",
    "password": "12345678",
    "host": "localhost",
    "database": "gestione_progetti"
}

connection = mariadb.connect(**conn_params)

cursor = connection.cursor(dictionary=True)

print("inserire i dati per la creazione del deliverable")


print("Quantita: ")
quantita = input("-->")


cursor.execute("INSERT INTO deliverables(quantita) VALUES (?)", (quantita,))

connection.commit()
connection.close()

print("Deliverable inserito con successo (solo Quantita inserita).")