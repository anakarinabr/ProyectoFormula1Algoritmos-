
class Producto():

    def __init__(self, name, price, cantidad):
        self.name = name 
        self.price = price
        self.cantidad = cantidad

    def show_attr(self):
        print(f'Name: {self.name}\nType: {self.type}\nPrice: {self.price}')