import pickle

class Modulo4():

    def __init__(self):
        self.carreras = []
        self.facturas = []

    def cargar_information(self): #Carga la información en los atributos

        with open('Carreras.txt', 'rb') as leer_carreras:
           self.carreras = pickle.load(leer_carreras)

        with open('Facturas.txt', 'rb') as leer_facturas:
           self.facturas = pickle.load(leer_facturas)

    def search_by_name(self): #Busca el proucto por su nombre
        name = input('Enter product name: ')
        while not ("".join(name.split(" ")).isalpha()):
            name = input("Try again: ")

        for x in self.carreras:
            for y in x.restaurantes:
                for m in y.items:
                    if m.name == name:
                        print(f'\n----- {y.name} -----'.upper())
                        m.show_attr()

    def search_by_type(self): #Se buscan los productos por tipo, si es bebida alcolica o no alcoholica, y si es comida rapida o de restaurante

        option = input('Would you like (1)Foods or (2)Drinks?: ')
        while option != '1' and option != '2':
            option = input('Try again. (1)Foods or (2)Drinks: ')

        if option == '1':
            option = 'food'
            tipo = input('Do you want search (1)Fast Food or (2)Restaurant food: ')
            while tipo != '1' and tipo != '2':
                tipo = input('Try again. (1)Fast or (2)Restaurant: ')
            if tipo == '1':
                tipo = 'fast'
            else: 
                tipo = 'restaurant'
        else: 
            option = 'drink'
            tipo = input('Do you want search (1)Alcoholic drinks or (2)Not alcoholic drinks: ')
            while tipo != '1' and tipo != '2':
                tipo = input('Try again. (1)Alcoholic or (2)Not alcoholic: ')
            if tipo == '1':
                tipo = 'alcoholic'
            else:
                tipo = 'not-alcoholic'

        print('      PRODUCTS      ')
        
       
        for x in self.carreras:
            for y in x.restaurantes:
                    restaurante = []
                    for m in y.items:
                        if m.type_p_v == tipo:
                            restaurante.append(m)
                        elif m.type_p_v == tipo:
                            restaurante.append(m)

                    if len(restaurante) != 0:    
                        print(f'\n----- {y.name} ------')
                        for i, x in enumerate(restaurante):
                            print('\n')
                            print(f'{i+1}.')
                            x.show_attr()
    
    def search_price(self): #Se buscan los productos en un rango de precio introducido por el usuario
        while True:
            try:
                menor = int(input('Enter lower price: '))
                mayor = int(input('Enter higher price: '))
                break
            except:
                print('Try again!')
    

        while menor > mayor and menor < 1 and mayor < 1:
            menor = int(input('Try again. Enter lower price: '))
            mayor = int(input('Try again. Enter higher price'))

        for x in self.carreras:
            for y in x.restaurantes:
                restaurante = []
                for m in y.items:
                    if m.price in range(menor, mayor+1):
                        restaurante.append(m)
                if len(restaurante) != 0:
                    print(f'\n----- {y.name} -----')
                    for i, n in enumerate(restaurante):
                        print(f'{i+1}.')
                        n.show_attr()

    def start(self): #Inicia el programa
    
            self.cargar_information()
            while True: 
                print('\n      Restaurant management'.upper())
                selection = input('1. Products by name\n2. Products by type\n3. Products by price\n4. Back to principal menu\n>>>>')

                if selection == '1':
                    self.search_by_name()
                elif selection == '2':
                    self.search_by_type()
                elif selection == '3':
                    self.search_price()
                elif selection == '4':
                    break
                else:
                    print('Oops! Try again.')