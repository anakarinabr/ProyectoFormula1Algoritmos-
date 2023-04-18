import requests
import pickle
import random
from Piloto import Piloto
from Constructor import Constructor
from Carrera import Carrera
from Circuito import Circuito
from Restaurant import Restaurante
from BebidaAlcoholica import BebidaAlcoholica
from BebidaNoAlcoholica import BebidaNoAlcoholica
from ComidaFast import ComidaFast
from ComidaRestaurant import ComidaRestaurant


class Modulo1():
    def __init__(self): #Esta es mi database que se llena a partir de los txt
        self.pilotos = []
        self.constructores = []
        self.carreras = []
        self.circuitos = []
        self.productos = []
        self.restaurantes = []

    def cargar_information(self): #Aqui se lee la información que está en los txt
        with open('Carreras.txt', 'rb') as leer_carreras:
            self.carreras = pickle.load(leer_carreras)

        with open('Pilotos.txt', 'rb') as leer_pilotos:
            self.pilotos = pickle.load(leer_pilotos)

        with open('Constructores.txt', 'rb') as leer_constructores:
            self.constructores = pickle.load(leer_constructores)

        with open('Circuitos.txt', 'rb') as leer_circuitos:
            self.circuitos = pickle.load(leer_circuitos)

    def information(self): #Método para acceder a la informción de las APIS
        #BUSQUEDA DE INFORMACION DE LAS APIS
        url_pilotos = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json"
        url_constructores = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json"
        url_carreras = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json" 
        
        #PAGE RESPONSES [200,202,404, ...]
        response_pilotos = requests.request('GET',url_pilotos)
        response_constructores = requests.request('GET',url_constructores)
        response_carreras = requests.request('GET',url_carreras)

        #JSON FILES 
        pilotos = response_pilotos.json()
        constructores = response_constructores.json()
        carreras = response_carreras.json()

        return pilotos, constructores, carreras
    
    def setting(self): #Pasar a objetoss
        pilotos, constructores, carreras = self.information()

        self.pilotos.clear()
        self.constructores.clear()
        self.carreras.clear()
        self.circuitos.clear()

        #PILOTOS
        for x in pilotos:
            id1 = x["id"]
            permanentNumber = x["permanentNumber"]
            code = x["code"]
            team = x["team"]
            first_name = x["firstName"]
            last_name = x["lastName"]
            date_of_birth = x["dateOfBirth"]
            nationality1 = x["nationality"]
            piloto_objeto = Piloto(id1, permanentNumber, code, team, first_name, last_name, date_of_birth, nationality1)
            self.pilotos.append(piloto_objeto)

        # CONSTRUCTORES
        for i in constructores: 
            id2 = i["id"]
            name2 = i["name"]
            nationality2 = i["nationality"]
            pilotos = []
            for m in self.pilotos:
                if m.team == id2:
                    pilotos.append(m)
            constructor_objeto = Constructor(id2, name2, nationality2, pilotos)
            self.constructores.append(constructor_objeto)

        # CIRCUITOS
        for z in carreras:
            name3 = z["circuit"]["name"]
            locality = z["circuit"]["location"]["locality"]
            country = z["circuit"]["location"]["country"]
            lat = z["circuit"]["location"]["lat"]
            long = z["circuit"]["location"]["long"]
            id3 = z["circuit"]["circuitId"]
            self.circuitos.append(Circuito(name3, locality, country, lat, long, id3))
     
        # PRODUCTS
        for x in carreras:
            for y in x["restaurants"]:
                for p in y["items"]:
                    cantidad = 5
                    name = p["name"]
                    type1 = p["type"].split(':')
                    price = float(p["price"])*(1+0.16)
                    if type1[0] == 'food':
                        if type1[1] == 'fast':
                            producto2 = ComidaFast(name, type1[0], price, type1[1], cantidad)
                        else:
                            producto2 = ComidaRestaurant(name, type1[0], price, type1[1], cantidad)
                    else:
                        if type1[1] == 'alcoholic':
                            producto2 = BebidaAlcoholica(name, type1[0], price, type1[1], cantidad)
                        else:
                            producto2 = BebidaNoAlcoholica(name, type1[0], price, type1[1], cantidad)

                    self.productos.append(producto2)
                    

        # RESTAURANTE
        for x in carreras:
            for y in x["restaurants"]:
                productos_rest = []
                name = y["name"]
                for p in y["items"]:
                    for m in self.productos:
                        if m.name == p['name']:
                            producto1 = m 
                            productos_rest.append(producto1)

                self.restaurantes.append(Restaurante(name, productos_rest))
                        

        # CARRERAS
        
        for p in carreras:
            restaurantes_por_carrera = []
            round = p["round"]
            name4 = p["name"]
            date = p["date"]
            circuitId = p["circuit"]["circuitId"]
            map = p["map"]

            for j in p["restaurants"]:
                for a in self.restaurantes:
                    if j["name"] == a.name:
                        restaurante = a
                        restaurantes_por_carrera.append(restaurante)

            for g in self.circuitos:
                if circuitId == g.id:
                    circuit = g

            self.carreras.append(Carrera(round, name4, circuit, date, map, restaurantes_por_carrera))

    def guardar_en_txt(self): #Acá se guarda, esto se ejecuta cuando el usuario quiere regresar al menu principal
        with open('Carreras.txt', 'wb') as carreras:
            pickle.dump(self.carreras, carreras)

        with open('Pilotos.txt', 'wb') as pilotos:
            pickle.dump(self.pilotos, pilotos)

        with open('Constructores.txt', 'wb') as constructores:
            pickle.dump(self.constructores, constructores)

        with open('Circuitos.txt', 'wb') as circuitos:
            pickle.dump(self.circuitos, circuitos)
        
        with open('Restaurantes.txt', 'wb') as restaurantes:
            pickle.dump(self.restaurantes, restaurantes)

    def search_information(self):  #Aqui se generan son las busquedas pedidas en los requerimientos
         print('----- SEARCH INFORMATION -----')
         while True:                
                    print('\n1. Constructor by country\n2. Pilots by constructor\n3. Races by country of the circuit\n4. Races per month\n5. Back')
                    selection = input('>>>>')

                    if selection == '1': #Contructor por su nacionalidad
                        print('------ Nationality -----'.upper())
                        list_1 = []
                        for m in self.constructores:
                            list_1.append(m.nationality)

                        list_1 = list(set(list_1))
                        for i, x in enumerate(list_1):
                            print(f'{i+1}. {x}')
                                                        
                        country = input("Enter the number that you looking for: ")
                        while not country.isnumeric() and int(country) < 1:
                            country = input('Ingreso inválido, intente de nuevo: ')

                        country = int(country) - 1
                        for index, u in enumerate(list_1):
                            if index == country:
                                country = u

                        print('Contructores: ')

                        for w in self.constructores:
                            if w.nationality == country:
                                print(f'    - {w.name}')

                        wish = input('Would you like to continue? ("Y" to yes, "N" to no): ').upper()

                        while wish != 'Y' and wish != 'N':
                                wish = input('Try again ("Y" to yes, "N" to no): ').upper()
                        
                        if wish == 'N':
                            break

                    elif selection == '2': #Pilotos por constructores
                        print('\n----- Constructors -----'.upper())
                        for index, value in enumerate(self.constructores):
                            print(f'{index + 1}. {value.name}')

                        while True:
                            try:                      
                                construc = int(input('Enter the number you looking for: ')) -1
                                break
                            except:
                                print('Ingreso inválido, intente de nuevo!')

                        print('Pilotos: ')
                        for index, value in enumerate(self.constructores):
                            if index == construc:
                                for i,x in enumerate(value.pilotos):
                                    print(f'{i +1}. {x.first_name} {x.last_name}')

                        wish = input('Would you like to continue? ("Y" to yes, "N" to no): ').upper()
                        while wish != 'Y' and wish != 'N':
                                wish = input('Try again ("Y" to yes, "N" to no): ').upper()                        
                        if wish == 'N':
                            break

                    elif selection == '3': #Carreras por los circuitos de los paises
                        countries = []
                        for x in self.carreras:
                            countries.append(x.circuit.country)
                        countries = list(set(countries))

                        print('----- Countries -----'.upper())
                        for ind, val in enumerate(countries):
                            print(f'{ind +1}. {val}')

                        country2 = input('Enter the number you looking for: ')

                        while not country2.isnumeric() and country2 < 1 and country > 22:
                            country2 = input('Sorry, something were wrong. Try again: ')

                        country2 = int(country2) -1

                        for inde, value in enumerate(countries):
                            if inde == country2:
                                country2 = value

                        for x in self.carreras:
                            if x.circuit.country == country2:
                                print('-------------------')
                                print(f'Name: {x.name}\nRound: {x.round}\nCircuit: {x.circuit.name}\nDate: {x.date}')
                                print('-------------------')

                        wish = input('Would you like to continue? ("Y" to yes, "N" to no): ').upper()
                        while wish != 'Y' and wish != 'N':
                                wish = input('Try again ("Y" to yes, "N" to no): ').upper()                        
                        if wish == 'N':
                            break
                    
                    elif selection == '4': #Carreras por meses

                        print("------ RACES' MONTHS ------") 

                        option = input('Enter the month number that you looking for (ex: 04 to April): ')

                        while not option.isnumeric() and int(option) < 1 and int(option) >13:
                            option = input('Something were wrong, try again: ')    

                        for x in self.carreras:
                            date_new = x.date.split('-')
                            if date_new[1] == option:
                                x.show_attr() 

                        wish = input('Would you like to continue? ("Y" to yes, "N" to no): ').upper()
                        while wish != 'Y' and wish != 'N':
                                wish = input('Try again ("Y" to yes, "N" to no): ').upper()                        
                        if wish == 'N':
                            break                          

                    elif selection == '5':
                        break
                    
                    else: 
                        print('Oops, try again!')
    
    def show_database(self): #Esta funcion está hecha para verificar que la información de la API se guardó correctamente
        print('----- SHOW DATEBASE -----')
        while True: 
                    
                    print('\n1. Races\n2. Circuits\n3. Constructors\n4. Pilots\n5. Back')
                    option = input('>>>>')

                    if option == '1':
                        for i,x in enumerate(self.carreras):
                            print(f'--- {i +1} ----')
                            x.show_attr()

                    elif option == '2':
                        for i,x in enumerate(self.circuitos):
                            print(f'--- {i +1} ---')
                            x.show_attr()
                    
                    elif option == '3':
                        for i,x in enumerate(self.constructores):
                            print(f'--- {i +1} ----')
                            x.show_attr()
                    
                    elif option == '4':
                        for i,x in enumerate(self.pilotos):
                            print(f'--- {i +1} ----')
                            x.show_attr()
                    
                    elif option == '5':
                        break
                    
                    else:
                        print('Oops, something were wrong!')
    
    def finish_races(self): #Acá se finalizan las carreras, se muestran únicamente si el atributo Podium es distinto de None

        print('\n             Races     '.upper())
        for i, x in enumerate(self.carreras):
            if x.podium == None:
                print(f'\n---- {i+1} ----')
                x.show_attr()

        while True:
            try:
                carrera = int(input('\nEnter the race number that you want to finish it: ')) -1
                break
            except:
                print('Oops, try again!')
        
        for i, x in enumerate(self.carreras): 
            podium_list = []
            puntaje = [25,18,15,12,10,8,6,4,2,1]

            if carrera == i: 
                while len(podium_list) < 10:  
                    ganador = random.choice(self.pilotos)
                    if podium_list.count(ganador) == 0:
                        podium_list.append(ganador)   #for loop se general los puestos al azar, con la condición de que no está ya dentro de la lista, para que no hayan repetidos

                x.podium = podium_list
                
                x.show_attr()
                print('\n--------- Podium ---------'.upper())
                for index, x in enumerate(podium_list):
                    print(f'{index+1}º {x.first_name} {x.last_name}:  {puntaje[index]} points')
                # SUMAR PUNTOS A OBJETOS PILOTOS
                for x in self.carreras:
                    if x.podium != None:
                        for index, piloto in enumerate(x.podium):
                            piloto.points += puntaje[index]
                
    def end_season(self):  #Acá sacamos el piloto y el contructor con mayor puntaje

        piloto_mayor = self.pilotos[0]
        constructor_mayor = self.constructores[0]

        print('\n--------- world champion ---------'.upper())
        for piloto2 in self.pilotos:
            if int(piloto_mayor.points) < piloto2.points:
                piloto_mayor = piloto2

        piloto_mayor.show_attr()


        print('\n--------- Constructor champion ---------'.upper())
        for constructor in self.constructores:
            for piloto in constructor.pilotos:
                constructor.points += piloto.points
        
        for constructor2 in self.constructores:
            if int(constructor_mayor.points) < constructor2.points:
                constructor_mayor = constructor2

        constructor_mayor.show_attr()

        print('\nCongratulations both!')

    def start(self): #Inicia el programa

        self.cargar_information()

        while True: 
            print('\n     Race and team management'.upper())
            selection = input('1. Update datebase\n2. Show database\n3. Search information\n4. Finish races\n5. End the season\n6. Back to principal menu\n>>>>')

            if selection == '1':
                self.information()
                self.setting()
            
            elif selection == '2':
                self.show_database()

            elif selection == '3':
                self.search_information()

            elif selection == '4':
                self.finish_races()

            elif selection == '5':
                self.end_season()

            elif selection == '6':
                self.guardar_en_txt()
                break
            else:
                print('Oops! Try again.')