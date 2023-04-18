from Producto import Producto

class Comida(Producto):
    def __init__(self, name, type_p, price, cantidad):
        self.type_p = type_p
        super().__init__(name, price, cantidad)