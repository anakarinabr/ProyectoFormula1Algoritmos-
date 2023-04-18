from Modulo1 import Modulo1
from Modulo2 import Modulo2
from Modulo3 import Modulo3
from Modulo4 import Modulo4
from Modulo5 import Modulo5
from Modulo6 import Modulo6
import os

def main():
    os.system('cls') #ESTO ES OPCIONAL, ES PARA LIMPIAR LA PANTALLA CADA QUE APAREZCA EL MENU
    while True: 
            print("""

            Welcome to the 2023 Formula 1 season:
                  -------- Menu ---------
                1. Race and team management.
                2. Tickets sales management.
                3. Attendance management.
                4. Restaurant management.
                5. Restaurant sales manegement.
                6. Management indicators (statistics)
                7. Exit""")
            option = input('''
            >>>>>''')

            if option == '1':
                app = Modulo1()
                app.start()

            elif option == '2':
                app = Modulo2()
                app.start()

            elif option == '3':
                app = Modulo3()
                app.start()

            elif option == '4':
                app = Modulo4()
                app.start()

            elif option == '5':
                app = Modulo5()
                app.start()

            elif option == '6':
                app = Modulo6()
                app.start()

            elif option == '7':
                print('\nSee you soon!')
                break
            else: 
                print('\nIngreso inválido, intente de nuevo!')

main()