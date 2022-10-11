from calculadora import Calculator

def main():
    operacion = Calculator(5,3)
    
    print(f'suma: {operacion.suma()}, resta: {operacion.resta()}, multiplication: {operacion.multiplication()}, división: {operacion.divide()}')
    

if __name__ == '__main__':
    main()