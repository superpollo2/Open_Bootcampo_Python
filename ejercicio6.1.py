class Vehiculo:
    color = None 
    ruedas = None
    puertas = None
    
    def __init__(self,color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
     
    def __str__(self):
        return (f'color: {self.color} ruedas: {self.ruedas} puertas: {self.puertas}' )   
        
class Coche(Vehiculo):
    velocidad = None 
    cilindrada = None
    
    def __init__(self,color, ruedas, puertas,velocidad,cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada =cilindrada
        
    def __str__(self) -> str:
        return (f'velocidad: {self.velocidad} cilindrada: {self.cilindrada} {super().__str__()}')
        
coche = Coche("azul", 4, 3, 120, 500)
print(coche.__str__())