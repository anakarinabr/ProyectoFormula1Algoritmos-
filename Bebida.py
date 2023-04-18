from Producto import Producto

class Bebida(Producto):
    def __init__(self, name, type_p, price, cantidad):
        self.type_p = type_p
        super().__init__(name, price, cantidad)

    def show_attr(self):
        print(f'Type: {self.type_p}')