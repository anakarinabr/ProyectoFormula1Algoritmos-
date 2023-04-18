import pickle


class Modulo3():
    def __init__(self):
        self.facturas = []
        self.carreras = []
    
    def cargar_information(self): #Se lee las txt y se guarda los atributos

        with open('Facturas.txt', 'rb') as leer_facturas:
           self.facturas = pickle.load(leer_facturas)

        with open('Carreras.txt', 'rb') as leer_carreras:
           self.carreras = pickle.load(leer_carreras)

    def guardar_en_txt(self): #Se guarda en el txt los atributos

        with open('Facturas.txt', 'wb') as facturas:
            pickle.dump(self.facturas, facturas)

        with open('Carreras.txt', 'wb') as carreras:
            pickle.dump(self.carreras, carreras)
    
    def validar_codigo(self): #Acá se valida el cliente con sus tickects
        print('--- USER DATA ---')

        name = input('Name: ').capitalize()
        while not ("".join(name.split(" ")).isalpha()):
            name = input("Try again: ")
                
        id = input("Id: ")
        while not id.isalnum() or int(id) < 1:
            id = input('Try again: ')
            
        contador = 0
        for x in self.facturas:
            if id == x.cliente.id:
                for i, m in enumerate(x.tickets):
                    if m.confirmado == False:
                        print(f'----- {i+1} -----')
                        m.show()
                        contador+=1

        while True:
            try: 
                ticket = int(input('Enter the ticket number you want to confirm: ')) - 1
                while ticket >= (contador-1) or ticket <= -1:
                    ticket = int(input('Try again:'))
                code = int(input('Enter ticket code: '))
                break
            except:
                print('Oops, something were wrong\n')


        for x in self.facturas:
            if name == x.cliente.name and id == x.cliente.id:
                for i, m in enumerate(x.tickets):
                    for x in self.carreras:
                        if code == m.number and m.confirmado == False and ticket == i and x.name == m.race.name:
                            print('\nVerified code!\n')
                            m.confirmado = True 
                            m.race.asistencia[m.type] += 1
                            x.asistencia[m.type] += 1
                            m.show()
                            break
                        if m.confirmado == True and i == ticket:
                            print('\nThis ticket is already used\n')
                                                    
    def start(self): #Inicia el programa
        self.cargar_information()
        while True: 
            print('\n      Attendance management'.upper())
            selection = input('1. Confirm ticket\n2. Back to principal menu\n>>>>')

            if selection == '1':
                self.validar_codigo()
            elif selection == '2':
                self.guardar_en_txt()
                break
            else:
                print('Oops! Try again.')
