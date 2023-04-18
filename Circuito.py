
class Circuito():

    def __init__(self, name,  locality, country, lat, long, id ):
        self.id = id
        self.name = name
        self.locality = locality
        self.country = country
        self.lat= lat
        self.long = long

    def show_attr(self):
        print(f'Id: {self.id}\nName: {self.name}\nLocality: {self.locality}\nCountry: {self.country}\nLatitud: {self.lat}\nLong: {self.long}')