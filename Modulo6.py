import pickle
from Vip import Vip


class Modulo6():
    def __init__(self):
        self.facturas = []
        self.carreras = []
        self.facturas_restaurantes = []
    
    def cargar_information(self): #Se lee la informacion de las API

        with open('Facturas.txt', 'rb') as leer_facturas:
           self.facturas = pickle.load(leer_facturas)

        with open('Carreras.txt', 'rb') as leer_carreras:
           self.carreras = pickle.load(leer_carreras)

        with open('Facturas_restaurantes.txt', 'rb') as leer_facturas_restaurante:
           self.facturas_restaurantes = pickle.load(leer_facturas_restaurante)

    def prom_gastado_vip(self): #Se saca la cantidad de gastada entre todos los clientes vip y luego lo divido entre la cantidad de clientes vip
        
        cantidad = 0
        gastado_total = 0

        for factura in self.facturas:
            gastado = 0.00
            for index, ticket in enumerate(factura.tickets):
                if type(ticket) == Vip and index == 0:
                    gastado += float(factura.total)
                    cantidad += 1
            for factura_restaurante in self.facturas_restaurantes:
                if factura.cliente.name == factura_restaurante.cliente.name:
                    gastado += factura_restaurante.total
            gastado_total +=gastado

        gastado_prom = gastado_total/cantidad
        print(f'\n------------------------\n The average spent by a VIP customer is: ${gastado_prom}\n------------------------')

    def tabla(self):  #Con una funcion lambda organizo mi lista se carreras de mejor a peor

        # Mostrar tabla con la asistencia a las carreras de mejor a peor, mostrando el nombre del carrera (nombre de los equipos), 
        # circuito en donde se juega, boletos vendidos, personas que asistieron y la relación asistencia/venta

        self.carreras.sort(key = lambda p: p.contar(), reverse= True)


        print('-----------------------------------------------------------------')
        for index, carrera in enumerate(self.carreras):
            vip= ''
            general = ''
            for asiento in carrera.asientos_ocupados['General']:
                general += f'{asiento} - '

            for asiento in carrera.asientos_ocupados['Vip']:
                vip += f'{asiento} - '

            if vip == '':
                vip = 'No se han vendido entradas'
            if general == '':
                general = 'No se han vendido entradas'

            personas = ''
            for comprador in carrera.compradores:
                personas += f'{comprador}, '
            if personas == '':
                personas = 'Ninguna'

            print(f'''
        {index +1}. {carrera.name}. 
                    - Circuit: {carrera.circuit.name}
                    - Tickets sold: 
                            Vip: {vip[0:-3]}
                            General: {general[0:-3]}
                    - People who attended: {personas}
                    - Assistance/sale ratio: {carrera.asistencia['Vip']+ carrera.asistencia['General']}/{len(carrera.asientos_ocupados['Vip'])+len(carrera.asientos_ocupados['General'])}''')

    def carrera_mayor_asistencia(self): #Acá busco la carrera con más asistencias y luego la muestra

        mayor_asistencia = self.carreras[0].asistencia['Vip'] + self.carreras[0].asistencia['General']
        mayor_carrera = self.carreras[0].name
        for carrera in self.carreras:
            if mayor_asistencia <= (carrera.asistencia['Vip'] + carrera.asistencia['General']):
                mayor_asistencia = (carrera.asistencia['Vip'] + carrera.asistencia['General'])
                mayor_carrera = carrera.name

        print(f'\n------------------------\n Most attended race is: {mayor_carrera}\n------------------------')
    
    def mayor_boletos_vendidos(self): #Acá busco la carrera con más boletos vendidos y luego lo muestro

        mayor_cantidad_de_boletos = len(self.carreras[0].asientos_ocupados['Vip']) + len(self.carreras[0].asientos_ocupados['General'])
        carrera = self.carreras[0].name
        for x in self.carreras:
            if mayor_cantidad_de_boletos < (len(x.asientos_ocupados['Vip']) + len(x.asientos_ocupados['General'])):
                mayor_cantidad_de_boletos = len(x.asientos_ocupados['Vip']) + len(x.asientos_ocupados['General'])
                carrera = x.name

        
        print(f'\n------------------------\n Race with most tickets sold: {carrera}\n------------------------')

    def productos_mas_vendidos(self): #Con una función lambda ordenos mis productos y muestro los mejores

        listproducts = []
        for carrera in self.carreras:
            for restaurant in carrera.restaurantes: 
                for producto in restaurant.items:
                    listproducts.append(producto)
        
        listproducts.sort(key = lambda p: p.cantidad_vendida, reverse= True)

        print(f'\n--------- Top 3 products ---------\n1. {listproducts[0].name} \n2. {listproducts[1].name}\n3. {listproducts[2].name}\n------------------------')

    def mejores_clientes(self): #Con una función lambda organizo mis clientes y muestro los mejores 3.

        self.facturas.sort(key = lambda p: p.contador_tickets1(), reverse= True)

        print(f'\n--------- Top 3 clients ---------\n1. {self.facturas[0].cliente.name} \n2. {self.facturas[1].cliente.name}\n3. {self.facturas[2].cliente.name}\n------------------------')

    def start(self): #Inicia
        self.cargar_information()

        while True: 
            print('\n     statistics.'.upper())
            selection = input('1. Average spent by a vip customer\n2. Race attendance\n3. Most assisted race\n4. Races with the most tickets sold\n5. Top 3 products\n6. Top 3 clients\n7. Back to principal menu\n>>>>')

            if selection == '1':
                self.prom_gastado_vip()
            elif selection == '2':
                self.tabla()
            elif selection == '3':
                self.carrera_mayor_asistencia()
            elif selection == '4':
                self.mayor_boletos_vendidos()
            elif selection == '5':
                self.productos_mas_vendidos()
            elif selection == '6':
                self.mejores_clientes()
            elif selection == '7':
                break
            else:
                print('Oops! Try again.')