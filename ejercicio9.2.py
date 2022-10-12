import functools
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_par(number):
    if number % 2 == 0:
          return True  

    return False

number_list = filter(check_par, numbers)

even_numbers = functools.reduce(lambda a,b : a+b, list(number_list))

print(even_numbers)


    