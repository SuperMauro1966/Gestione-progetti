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

print("nome: ")
nome=input("-->")


print("descrizione: ")
descrizione=input("-->")
print("data inizio:")
data_inizio=input("-->")
print("data fine: ")
data_fine=input("-->")

cursor.execute("INSERT INTO progetto(Nome, Descrizione, Data_Inizio, Data_Fine ) VALUES (?,?,?,?)", (nome, descrizione, data_inizio, data_fine))
 
connection.commit()

connection.close()
