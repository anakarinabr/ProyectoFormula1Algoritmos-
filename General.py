from Entrada import Entrada

class General(Entrada):
    def __init__(self, race, number, type, costo, asiento):
        self.type = type
        self.costo = costo
        self.confirmado = False
        super().__init__(race, number, asiento)

    def show(self):
        print(f'Race: {self.race.name}\nType ticket: {self.type}Seat: {self.asiento}')
        