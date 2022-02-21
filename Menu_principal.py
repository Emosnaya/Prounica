
from random import randint
from telnetlib import DO
from ClassPokemon1018 import Fairy, Psychic, Water
from Impresion_graficas import mostrar_gráficas
from classPokemon import Pokemon
from classPokemons18 import Electric, Fire
from pelea import pelea
#Introducción al usuario
print("BIENVENIDO A TU POKEDEX\n")
print("¿QUE DESEA HACER?")
#Menú de opciones
def menu():
    #Validacion de lo que ingrese el usuario
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

salir = False
opcion = 0
#Ciclo del menú
while not salir:
    #opciones para el usuario
    print ("1. Ver lista de pokemones")
    print ("2. Pelea entre dos pokemones")
    print ("3. Salir")

    opcion = int(input("Elige una opcion\n"))

    #Se llama la función de la impresion de estadisticas y graficas
    if opcion == 1:
        mostrar_gráficas()
    #Se llama la funcion de pelea entre dos pokemones
    elif opcion == 2:
        pelea()
    #Salir del ciclo
    elif opcion == 3:
        salir = True
        print("RECUERDA TRATAR CON AMOR TUS POKEMONES")
    #En caso de no seleccionar una opcion correcta
    else:
        print ("Introduce un numero entre 1 y 3")

print ("Fin")



