import pickle
import random
from Cliente import Cliente
from Vip import Vip
from General import General
from Factura_Entradas import Factura_Entradas

class Modulo2():
    def __init__(self):
        self.carreras = []
        self.numbers = []
        self.facturas = []

    def clear_facturas(self): #Acá limpio mi txt cada vez que quiere poner desde cero el programa
        self.facturas.clear()
        for x in self.carreras:
            x.asientos_ocupados['General'].clear()
            x.asientos_ocupados['Vip'].clear()

    def cargar_information(self): #Se leen los txt y se agregan los objetos a las variables

        with open('Carreras.txt', 'rb') as leer_carreras:
            self.carreras = pickle.load(leer_carreras)

        with open('Facturas.txt', 'rb') as leer_facturas:
            self.facturas = pickle.load(leer_facturas)

    def guardar_en_txt(self): #Se guarda la información de las variables en los txt

        with open('Facturas.txt', 'wb') as facturas:
            pickle.dump(self.facturas, facturas)

        with open('Carreras.txt', 'wb') as carreras:
            pickle.dump(self.carreras, carreras)
    
    def pedir_datos_cliente(self):  #Es llamada en self.generar_factura
        # DATOS CLIENTE
        name = input('Name: ').title()
        while not ("".join(name.split(" ")).isalpha()):
            name = input("Try again: ")
               
        id = input("Id: ")
        while not id.isnumeric():
            id = input('Try again: ')

        age = (input('Age: '))
        while not age.isnumeric():
            age =input('Try again: ')
        return name, id, age

    def num_ondulado(self, id): #Acá compruebo que la cedula sea un numero ondulado para aplicar el descuento o no, es llamada en self.calcular_montos
        
        ondulado = False

        id_new =  list(id)
        list1 = id_new[0::2]
        list2 = id_new[1::2]

        if len(set(list1)) == 1 and len(set(list2)) == 1:
            ondulado = True
            print(''''
            Congratulations, you have acquired a 50''','''%''',''' discount
            ''')

        return ondulado
    
    def generar_ticket(self, race, type2): #Aquí se generan los tickets con su código único y es llamada en self.generar_factura
        # DATOS TICKETS
        while True:
            number = int(random.random()*4000000000)
            if self.numbers.count(number) == 0:
                self.numbers.append(number)
                break 

        if type2 == '1':
            costo = 340
            asiento = self.mapa_def(race, 'vip')
            ticket = Vip(race, number, 'Vip', costo, asiento)

        elif type2 == '2':
            costo = 150
            asiento = self.mapa_def(race, 'general')
            ticket = General(race, number, 'General', costo, asiento)

        return ticket, asiento

    def mapa_def(self, race, type2): #Genera una matriz que muestra el numero de asientos segun la capacidad del circuito y es llamada en generar_tickect
        
        diccionario = {1: 'A', 2: 'B', 3: 'C', 4 : 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L' ,13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18 : 'R' , 19:'S', 20:'T', 21: 'U', 22: 'V', 23: 'W', 24: 'Y', 25: 'Z'}
    
        mapa = []
        for x in range(1, race.map[type2][0]+1):
            filas = []
            for m in range(1, race.map[type2][1]+1):
                asiento = str(m) + diccionario[x]
                filas.append(asiento)
            mapa.append(filas)

        for x in race.asientos_ocupados[type2.capitalize()]:
            for y in mapa:
                for i,m in enumerate(y):
                    if x == m:
                        y[i] = 'X'


        mapa2 = []
        for x in mapa:
            for y in x:
                mapa2.append(y)

        if len(list(set(mapa2))) != 1:
            print('\n')
            for x in mapa:
                show = ''
                for y in x:
                    show += f'{y} - '
                print(show[0:-3])

            option = input('\nEnter the seat: ').upper()
            while mapa2.count(option) == 0:
                option = input('Try again: ').upper()

            return option 
    
    def show_tickets(self): #Me muestra los facturas que tengo registradas, ya que dentro de una factura pueden haber varias entradas
        for i, x in enumerate(self.facturas):
            print(f'----- {i+1} -----')
            x.show()
            print('\n')

    def calcular_montos(self, tickets_por_cliente, cliente): #Acá calculo el monto toal de la factura con la cantidad de tickects que haya comprado el cliente

        subtotal = 0
        descuento = 0
        iva = 16
        for x in tickets_por_cliente:
            subtotal += x.costo

        ondulado = self.num_ondulado(cliente.id)

        if ondulado:
            descuento += 50

        total =  subtotal*(1 + 0.16 - (descuento/100))

        return subtotal, iva, descuento, total
    
    def generar_factura(self): #Función principal de la facturas para entradas, se crea los clientes y los tickects
        
        tickets_por_cliente = []
        name, id, age = self.pedir_datos_cliente()
        cliente = Cliente(name, id, age)

        print('\n         Races           '.upper())
        for i,x in enumerate(self.carreras):
            if x.podium == None:
                print(f'--- {i +1} ----')
                x.show_attr()
                print('\n')

        while True:
            try:
                selection = int(input("What race's tickects do you want: ")) -1
                while selection >= 23:
                    selection = int(input('Try again: ')) -1
                break
            except:
                print('Oops, try again: ')

        for i,x in enumerate(self.carreras):
            if i == int(selection):
                race = x

        print('\nTicket type')

        type2 = input('1. Vip\n2. General\n>>>')
        while type2 != '2' and type2 != '1':
            type2 = input('Try again: ')
        asientos = []

        while True:
            ticket, asiento = self.generar_ticket(race, type2)
            tickets_por_cliente.append(ticket)
            wish = input('Would you like other ticket for same race? ("Y" to yes, "N" to no): ').upper()
            while wish != 'Y' and wish != 'N':
                wish = input('Try again ("Y" to yes, "N" to no): ').upper()
            asientos.append(asiento)
            race.asientos_ocupados[ticket.type].append(asiento)
            if wish == 'N':
                break
            
        
        subtotal, iva, descuento, total = self.calcular_montos(tickets_por_cliente, cliente)

        factura = Factura_Entradas(cliente, tickets_por_cliente, subtotal, iva, descuento, total)
        factura.show()

        wish2 = input('Your ticket is ready. Are you sure of your purchase? ("Y" to yes, "N" to no): ').upper()
        while wish2 != 'Y' and wish2 != 'N':
            wish2 = input('Try again ("Y" to yes, "N" to no): ').upper()

        if wish2 == 'Y':
            for carrera in self.carreras:
                if carrera.name == race.name:
                    carrera.compradores.append(factura.cliente.name)

            self.facturas.append(factura)           
            print('\nYour purchase has been processed!')

        if wish2 == 'N':
            for x in asientos:
                for i, m in enumerate(race.asientos_ocupados[ticket.type]):
                    if x == m:
                        race.asientos_ocupados[ticket.type].pop(i)

    def start(self):  #Inicia el programa
        self.cargar_information()
        while True: 
            print('\n      Tickets sales management'.upper())
            selection = input('1. Tickets sales\n2. Show commercial invoice\n3. Clear bills\n4. Back to principal menu\n>>>>')

            if selection == '1':
                print('Information')
                self.generar_factura()
            elif selection == '2':
                self.show_tickets()
            elif selection == '3':
                self.clear_facturas()
            elif selection == '4':
                self.guardar_en_txt()
                break
            else:
                print('Oops! Try again.')