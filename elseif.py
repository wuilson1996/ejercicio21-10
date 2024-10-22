# Algoritmo para entrar al cine

edad1 = int(input("Ingresa edad 1: "))
edad2 = int(input("Ingresa edad 2: "))

if edad1 >= 18 and edad1 <= 30: # edad entre 18 y 30, el 30 no lo toma.
    print("Persona1 entra al cine")
else:
    print("Persona1 no entra al cine")

if edad2 >= 18 and edad2 <= 30: # edad entre 19 y 29, el 30 no lo toma.
    print("Persona2 entra al cine")
else:
    print("Persona2 no entra al cine")