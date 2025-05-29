import mariadb

conn_params= {
    "user" : "root",
    "password" : "12345678",
    "host" : "localhost",
    "database" : "gestione_progetti"
}
 
connection= mariadb.connect(**conn_params)

cursor = connection.cursor(dictionary=True)

print("inserire i dati per la creazione del progetto")
while True:
    print("nome: ")
    nome=input("-->")

    cursor.execute("SELECT COUNT(*) FROM progetto WHERE Nome = ?", (nome,))

    result = cursor.fetchone()
    count = result['COUNT(*)']

    if count > 0:
        print("Nome già esistente. Inserisci un nome diverso.")
    elif nome == "":
        print("Il nome non può essere vuoto.")
    else:
        break

print("descrizione: ")
descrizione=input("-->")
print("data inizio:")
data_inizio=input("-->")
print("data fine: ")
data_fine=input("-->")

cursor.execute("INSERT INTO progetto(Nome, Descrizione, Data_Inizio, Data_Fine ) VALUES (?,?,?,?)", (nome, descrizione, data_inizio, data_fine))
 
connection.commit()

connection.close()
