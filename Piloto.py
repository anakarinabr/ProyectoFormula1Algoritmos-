
class Piloto:

    def __init__(self, id, permanentNumber, code, team, first_name, last_name, date_of_birth, nationality):
        self.id = id
        self.permanentNumber = permanentNumber
        self.code = code
        self.team = team
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.nationality = nationality
        self.points = 0

    def show_attr(self):
        print(f'\nName : {self.first_name}\nLast name: {self.last_name}\nDate of birth: {self.date_of_birth}\nNationality: {self.nationality}\nCode: {self.code}\n Points: {self.points}')