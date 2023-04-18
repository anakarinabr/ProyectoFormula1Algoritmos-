
class Factura_Entradas():

    def __init__(self, cliente, tickets,  subtotal, iva, descuento, total):
        self.cliente = cliente 
        self.subtotal = subtotal
        self.descuento = descuento
        self.iva = iva 
        self.total = total
        self.tickets = tickets

    def contador_tickets1(self):
        tickets = 0
        for x in self.tickets:
            tickets += 1

        return tickets

    def show(self): 
        asientos = ''
        for x in self.tickets:
            race = x.race
            tipo = x.type
            asientos += f'{x.asiento}: {x.number} '
            
        # Imprime la factura proveniente de una compra de objetos
        print(f"""
            ************* BILL *************
            --------------------------------
                     User Data 
            Name: {self.cliente.name}
            Id: {self.cliente.id}
            Age: {self.cliente.age} years
            ---------------------------------
                    Ticket Data
            Race: {race.name}
            Ticket type: {tipo}
            Seats: {asientos}
            ----------------------------------
            Discount: {self.descuento}%    TAX: {self.iva}%
                    Sub Total: ${self.subtotal}
                    Total: ${self.total}
            
            """)
