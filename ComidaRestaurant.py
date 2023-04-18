from Comida import Comida

class ComidaRestaurant(Comida):

    def __init__(self, name, type_p, price, type_p_v, cantidad):
        self.type_p_v = type_p_v
        self.cantidad_vendida = 0
        super().__init__(name, type_p, price, cantidad)

    def show_attr(self):
        print(f'Name: {self.name}\nType product: {self.type_p} - {self.type_p_v}\nPrice: ${self.price}')