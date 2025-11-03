from dataclasses import dataclass

# Classe che mappa la tabella Business del database Yelp
# secondo il pattern DAO (eventualmente anche relazioni, con ORM)

@dataclass
class Business:
    business_id : str
    full_address : str
    active : str
    categories : str
    city : str
    review_count : int
    business_name : str
    neighborhoods : str
    latitude : float
    longitude : float
    state : str
    stars : float

    def __str__(self):
        return self.business_name+" "+str(self.stars)

    def __eq__(self, other):
        return self.business_id == other.business_id

    def __hash__(self):
        return hash(self.business_id)