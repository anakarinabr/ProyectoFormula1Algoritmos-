
class Factura_restaurante(): 

    def __init__(self, cliente, productos,  subtotal, descuento, total):
        self.cliente = cliente 
        self.subtotal = subtotal
        self.descuento = descuento 
        self.total = total
        self.productos = productos

    def show(self): 
        productos = ''
        for x in self.productos:
            productos += f'''{x.name}.....${x.price}      
            '''
            
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
            Products: 
            {productos}
            ---------------------------------
            Discount: {self.descuento}%  
                    Sub Total: ${self.subtotal}
                    Total: ${self.total}
            
            """)
