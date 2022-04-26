# Ejercicio 3
# Escribe un programa en donde pidas por teclado el nombre y el año de nacimiento de la persona y muestre como resultado el siguiente mensaje:
# {nombre} debe cumplir o cumplio {edad} años este año 

year = 2022
name = input('ingrese su nombre: ')
born_year = int(input('Ingrese su año de nacimiento: '))

age = year - born_year

print(f'{name} debe cumplir o cumplio {age} años este año')