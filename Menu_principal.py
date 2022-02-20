
from random import randint
from ClassPokemon1018 import Fairy, Psychic, Water
from classPokemon import Pokemon
from classPokemons18 import Electric, Fire
charizar = Fire('Charizard','6','Fuego/Volador','1.7m','90.5kg','H/M','Llama',7, 3,5, 'Mar LLamas' )
Mew = Psychic('Mew','151', 'Psíquico','0.4m','4kg','desconocido', 'Nueva especie', 7, 4,5, 'sincornía')
Togepi = Fairy('Togepi','175','Hada', '0.3m','1.5kg','H/M', 'Bolaclavos',5, 2, 3, 'Dicha')
totodile = Water('Totodile', '158', 'Agua', '0.6m','9.5kg', 'H/M','Fauces', 5, 3,4,'Torrente')
zapdos = Electric('Zapdos', '145', 'Electrico', '1.6m', '52.6kg','Desconocido', 'Electrico',8,4,5,'Presión' )


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
        print ("Seleccione el pokemon del cual desea saber sus estadisticas")
        
    elif opcion == 2:
        print ("Escoge dos pokemones para pelear")
        pokemons = {
            1: charizar.nombre,
            2: Mew.nombre,
            3: Togepi.nombre,
            4: totodile.nombre,
            5: zapdos.nombre 
            }
        for clave, valor in pokemons.items():
            print(f'{clave}: {valor}')

        player1 = int(input('Pokemon 1: '))
        player2 = int(input('Pokemon 2: '))

        print(f'Pelea entre {pokemons[player1]} y {pokemons[player2]}' )
        vida1 = 10
        golpe =  randint(1,3)
        while(vida1):
            print(f'Ataque de {pokemons[player1]} ')
            if golpe == 1 :
                print('Ataque normal')
                vida1 = vida1-3
            elif golpe == 2:
                print('Ataque especial')
                vida1 = vida1-4
            else:
                print('Ataque faliido')
            

        break
    elif opcion == 3:
        salir = True
        print("RECUERDA TRATAR CON AMOR TUS POKEMONES")
    else:
        print ("Introduce un numero entre 1 y 3")

print ("Fin")