import pickle
from BebidaAlcoholica import BebidaAlcoholica
from Factura_Restaurante import Factura_restaurante

class Modulo5():
    def __init__(self):
        self.facturas_restaurantes = []
        self.carreras = []
        self.facturas = []
    
    def cargar_information(self): #Lee las txt y carga esos objetos en los atributos

        with open('Facturas.txt', 'rb') as leer_facturas:
           self.facturas = pickle.load(leer_facturas)

        with open('Carreras.txt', 'rb') as leer_carreras:
           self.carreras = pickle.load(leer_carreras)

        with open('Facturas_restaurantes.txt', 'rb') as leer_facturas_restaurante:
           self.facturas_restaurantes= pickle.load(leer_facturas_restaurante)

    def guardar_en_txt(self):   #Guarda la informacion de los atributos en las txt

        with open('Facturas.txt', 'wb') as facturas:
            pickle.dump(self.facturas, facturas)

        with open('Carreras.txt', 'wb') as carreras:
            pickle.dump(self.carreras, carreras)

        with open('Facturas_restaurantes.txt', 'wb') as facturas_restaurantes:
            pickle.dump(self.facturas_restaurantes, facturas_restaurantes)
    
    def show_bills(self): #Muestra las facturas de restaurantes que estan registradas
        for index,x in enumerate(self.facturas_restaurantes):
            print(f'\n{index +1}')
            x.show()            

    def clear_facturas(self): #Acá se limpian las facturas para poner el programa desde cero
        self.facturas_restaurantes.clear()
    
    def verificacion(self): #Verificacion cliente vip y es llamada en self.venta_productos()
        m = None
        verificacion = False
        name = input('Name: ').title()
        while not ("".join(name.split(" ")).isalpha()):
            name = input("Try again: ")
               
        id = input("Id: ")
        while not id.isalnum() and int(id) < 1:
            id = input('Try again: ')

        for x in self.facturas:
            if x.cliente.id == id:
                m = x
                for y in x.tickets:
                    if y.type == 'Vip':
                        verificacion = True
                        break
        return verificacion, m
    
    def num_perfecto(self, n):  # Esto returna un bool que me permite aplicar los descuentos en la función self.calcular_montos()
        p = False
        divisores = []

        for d in range(1,int(n)):
            if int(n)%d == 0:
                divisores.append(d)

        if sum(divisores) == int(n):
            p = True

        return p
    
    def calcular_montos(self, listproductos, cliente, listcantidades): #Acá se calculan los montos de las factura de restaurante

        subtotal = 0
        descuento = 0

        for x in range(0, len(listproductos)):
            subtotal += listproductos[x].price*int(listcantidades[x])

        perfecto = self.num_perfecto(cliente.id)

        if perfecto:
            descuento += 15

        total = subtotal*(1 - (descuento/100))

        return subtotal, descuento, total

    def venta_productos(self):  #Acá la estructura general de la compra de productos

        verificacion, factura = self.verificacion()
        products = []
        cantidades = []

        if verificacion:
                for index, ticket in enumerate(factura.tickets):
                    if index == 1: 
                        for n in ticket.race.restaurantes:
                            print(f'---- {n.name} ----')
                            for i,c in enumerate(n.items):
                                if not c.cantidad == 0:
                                    if int(factura.cliente.age) >= 18:
                                        print(f'{i+1}.')
                                        c.show_attr()
                                    if int(factura.cliente.age) < 18:
                                        if type(c) != BebidaAlcoholica:
                                            print(f'{i+1}.')
                                            c.show_attr() 
                while True: 
                    selection = input('\nEnter the product name: ')
                    cantidad = input('Amount you want (No more than 5): ')
                    while not cantidad.isnumeric() or int(cantidad) > 5:
                        cantidad = input('Try again: ')

                    cantidad = int(cantidad)
                    cantidades.append(cantidad)

                    for carrera in self.carreras:
                        for restaurante in carrera.restaurantes:
                            for producto in restaurante.items:
                                if producto.name == selection:
                                    products.append(producto)
                                    producto.cantidad -= cantidad
                                    producto.cantidad_vendida += cantidad
                    

                    wish = input('Would you like product? ("Y" to yes, "N" to no): ').upper()
                    while wish != 'Y' and wish != 'N':
                        wish = input('Try again ("Y" to yes, "N" to no): ').upper()

                    if wish == 'N':
                        break
                    
                subtotal, descuento, total = self.calcular_montos(products, factura.cliente , cantidades)

                factura = Factura_restaurante(factura.cliente, products, subtotal, descuento, total)
                print('\n')
                factura.show()
                confirmación = input("\nYour bill is ready. Are you sure of your purchase? ('Y' to yes, 'N' to no): ").upper()
                if confirmación == 'Y':
                    self.facturas_restaurantes.append(factura)
               
                                    
        else:
            print("This ticket isn't available to buy in restaurants")

    def start(self): #Inicia el programa 
        self.cargar_information()

        while True: 
            print('\n     Restaurant sales manegement.'.upper())
            selection = input('1. Restaurants sales\n2. Show restaurants bill\n3. Clear restaurants bills\n4. Back to principal menu\n>>>>')

            if selection == '1':
                self.venta_productos()
            
            elif selection == '2':
                self.show_bills()
            
            elif selection == '3':
                self.clear_facturas()

            elif selection == '4':
                self.guardar_en_txt()
                break
            else:
                print('Oops! Try again.')
