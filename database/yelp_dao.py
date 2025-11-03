from database.db_connect import DBConnect
import mysql.connector

# LINK DA CUI SCARICARE LO SCRIPT SQL ED I FILE CSV PER CREARE E POPOLARE IL DATABASE YELP
# https://www.dropbox.com/scl/fi/e85q3n1kc9nwmphw2d8e6/Yelp.zip?rlkey=lwjeqf98lvt6wro37157mkmxp&st=vke2n7ys&dl=0

# Classe che si occupa dell'interazione con il database secondo il pattern DAO

from model.business import Business

# Metodi DAO per la lettura dei dati dal database usando query parametrizzate "on demand"
class YelpDao:
    def __init__(self):
        pass

    @staticmethod
    def read_businesses_with_stars(num_stars):
        print("Executing read from database using SQL query")
        results = []
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            # Query parametrizzata, richiamata ogni volta che l'utente cambia il numero di stelle nella casella dropdown
            query = """SELECT * 
                       FROM Business
                       WHERE stars >= %s"""
            cursor.execute(query, (num_stars,))
            for row in cursor:
                # Posso restituire direttamente una collezione delle righe lette dal cursore (come dizionari) ...
                # ... oppure creare oggetti di tipo Business da ogni riga e restituire una collezione di quelli
                business = Business(row["business_id"], row["full_address"], row["active"], row["categories"], row["city"], row["review_count"],
                                    row["business_name"], row["neighborhoods"], row["latitude"], row["longitude"], row["state"], row["stars"])
                results.append(business)

            cursor.close()
            cnx.close()
            return results


    # Metodi DAO per la lettura dei dati dal database una volta soltanto all'inizio

    @staticmethod
    def read_all_businesses():
        print("Executing read from database using SQL query")
        results = []
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            # Una sola query, con cui si leggono tutte le righe (si selezioneranno poi quelle che interessano es. con un if)
            query = """SELECT * 
                       FROM Business"""
            cursor.execute(query)
            for row in cursor:
                # Posso creare oggetti di tipo Business
                business = Business(row["business_id"], row["full_address"], row["active"], row["categories"],
                                        row["city"], row["review_count"],
                                        row["business_name"], row["neighborhoods"], row["latitude"], row["longitude"],
                                        row["state"], row["stars"])
                results.append(business)

            cursor.close()
            cnx.close()
            return results
