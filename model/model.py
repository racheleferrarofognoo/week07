from database.yelp_dao import YelpDao

# Classe che implementa il Model del pattern MVC (con altre classi nel package model)

class Model:
    def __init__(self):
        self._businesses = [] # Lista di tutti i business nel database

    # Metodo del Model che chiama il metodo corrispondente del DAO
    # Per leggere tutte le righe della tabella Business con numero di star
    # maggiore o uguale a quello passato come parametro e restituisce
    # una collezione di oggetti Business

    """
    def get_businesses_with_stars(self, num_stars):

        #Leggo le righe dalla tabella Business con DAO
        businesses = YelpDao.read_businesses_with_stars(num_stars)
        return businesses
    """

    # Metodo alternativo del Model che usa il metodo anonimo del DAO
    # per leggere tutte le righe della tabella Business, e non solo
    # quelle con un particolare numero di stars

    # Quanto letto, una volta sola, dal database è memorizzato in
    # una struttura dati del Model, alla quale si potrà fare accesso
    # quando necessario, eventualmente filtrando i dati, es. con if

    def get_all_businesses(self):
        if len(self._businesses) == 0: # Se non già letto dal database
            self._businesses = self._businesses = YelpDao.read_all_businesses()
        else:
            print("No need to read again from database using SQL query")
        return self._businesses
