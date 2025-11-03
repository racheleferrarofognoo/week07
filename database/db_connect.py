import mysql.connector
from mysql.connector import errorcode
from mysql.connector.aio import MySQLConnectionPool

# Classe di supporto per gestire la/e connessione/i al database (con pooling)

class DBConnect:
    _cnxpool = None # Variabile di classe e non di istanza

    def __init__(self):
        raise RuntimeError("DBConnect class shall not be instantiated! Call method get_connection() instead")

    @classmethod
    def get_connection(cls):
        #cnx = mysql.connector.connect(option_files=
        #                              "./database/db.cnf")

        #return cnx
        if cls._cnxpool is None:
            try:
                cls._cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
                                          pool_size = 3,
                                          option_files="./database/db.cnf")
                return cls._cnxpool.get_connection()
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                    return None
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                    return None
                else:
                    print(err)
                    return None
        else:
            return cls._cnxpool.get_connection()