
from random import randint
from telnetlib import DO
from ClassPokemon1018 import Fairy, Psychic, Water
from Impresion_graficas import mostrar_gráficas
from classPokemon import Pokemon
from classPokemons18 import Electric, Fire
from pelea import pelea
#Declaracion de los 5 pokemones
charizar = Fire('Charizard','6','Fuego/Volador','1.7m','90.5kg','H/M','Llama',7, 3,5, 'Mar LLamas', 'Hielo', 'Agua')

Mew = Psychic('Mew','151', 'Psíquico','0.4m','4kg','desconocido', 'Nueva especie', 7, 4,5, 'sincornía', 'Luchador', 'Metal')

Togepi = Fairy('Togepi','175','Hada', '0.3m','1.5kg','H/M', 'Bolaclavos',5, 2, 3, 'Dicha', 'Luchador', 'Metal')

totodile = Water('Totodile', '158', 'Agua', '0.6m','9.5kg', 'H/M','Fauces', 5, 3,4,'Torrente', 'Fuego', 'Electricidad')

zapdos = Electric('Zapdos', '145', 'Electrico', '1.6m', '52.6kg','Desconocido', 'Electrico',8,4,5,'Presión', 'Agua', 'Suelo' )


print("BIENVENIDO A TU POKEDEX\n")
print("¿QUE DESEA HACER?")
def menu():

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

while not salir:

    print ("1. Ver lista de pokemones")
    print ("2. Pelea entre dos pokemones")
    print ("3. Salir")

    opcion = int(input("Elige una opcion\n"))

    if opcion == 1:
        mostrar_gráficas()
        #pokemones = DataFrame() 
        #pokemones.df"""
        #print 
        print ("Seleccione el pokemon del cual desea saber sus estadisticas")
        
    elif opcion == 2:
        pelea()

        break
    elif opcion == 3:
        salir = True
        print("RECUERDA TRATAR CON AMOR TUS POKEMONES")
    else:
        print ("Introduce un numero entre 1 y 3")

print ("Fin")



