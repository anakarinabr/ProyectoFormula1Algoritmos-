

class Constructor:
    def __init__(self, id, name, nationality, pilotos):
        self.id = id
        self.name = name 
        self.nationality = nationality
        self.pilotos = pilotos
        self.points = 0

    def show_attr(self):
        print(f'Id: {self.id}\nName: {self.name}\nNationality: {self.nationality}\nPilotos: {self.show_pilotos()}')

    def show_pilotos(self):
        names = ''
        for x in self.pilotos:
            names += f'{x.first_name} {x.last_name}, '
        return names[0:-2]