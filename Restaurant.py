
class Restaurante():
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def show_attr(self):
        print(f'Name: {self.name}\nItems: {self.items}')