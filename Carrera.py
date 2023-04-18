

class Carrera():
    def __init__(self, round, name3, circuit, date, mapa, restaurantes):
        self.round = round
        self.name = name3
        self.circuit = circuit
        self.date = date
        self.podium = None
        self.map = mapa
        self.restaurantes = restaurantes
        self.asientos_ocupados = {'Vip': [], 'General': []}
        self.asistencia = {'Vip': 0, 'General': 0}
        self.compradores =[]

    def show_attr(self):
        print(f'Name: {self.name}\nRound: {self.round}\nCircuit: {self.show_circuit()}\nDate: {self.date}\n')

    def show_circuit(self):
        return f'{self.circuit.name}. Locality: {self.circuit.locality}, {self.circuit.country}'
    
    def contar(self):
        return self.asistencia['Vip'] + self.asistencia['General']
    
