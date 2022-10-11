class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota
    
    def aprobar_curso(self):
        if self.nota >= 3: print (f'aprobo con {self.nota}') 
        else: print(f'reprobo con {self.nota}') 
        
aprobo = Alumno("julian Cataño", 4.5)
aprobo.aprobar_curso()