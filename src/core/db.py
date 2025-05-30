import mariadb
from atexit import register


__all__ = ['conn',]

_conn_params= {
    "user" : "root",
    "password" : "12345678",
    "host" : "localhost",
    "database" : "gestione_progetti"
}
 
conn= mariadb.connect(**_conn_params)
register(conn.close)

