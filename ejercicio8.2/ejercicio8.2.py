
class Vehiculo:
    
    def __init__(self, placa, marca):
        self.placa = placa
        self.marca = marca
        
    def __str__(self):
        return (f'placa: {self.placa}, marca: {self.marca}')
    
    
auto = Vehiculo('54D1E', 'TOYOTA')

txt = open('Vehiculos.txt', 'a')
txt.write(f'{auto.__str__()}\n')
txt.close()