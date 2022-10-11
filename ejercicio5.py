
def leap_year(year):
    leap_year= int(year)
    if year.isnumeric():
       if  not leap_year % 4  and (leap_year % 100 or not leap_year % 400 ):
        print("es bisiesto")
       else:
        print("no es bisiesto")
           
    else:
        print("Usted ha ingresado un dato erroneo")

year= input("ingrese un año ")
leap_year(year)