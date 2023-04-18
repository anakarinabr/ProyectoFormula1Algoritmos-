

class Entrada():
    def __init__(self, race, number, asiento):
        self.race = race 
        self.number = number
        self.asiento = asiento
        self.confirmado = False


    def show_attr(self):
        print(f'Race: {self.race.name}\nSeat: {self.asiento}\nCode: {self.number}')

