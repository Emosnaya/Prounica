from random import randint
from ClassPokemon1018 import Fairy, Psychic, Water
from classPokemon import Pokemon
from classPokemons18 import Electric, Fire
#Se declaran los objetos pokemon y sus atributos
charizar = Fire('Charizard','6','Fuego','1.7m','90.5kg','H/M','Llama',7, 3,5, 'Mar LLamas', 'Hielo', 'Agua' )

Mew = Psychic('Mew','151', 'Psíquico','0.4m','4kg','desconocido', 'Nueva especie', 7, 4,5, 'sincornía', 'Luchador', 'Metal')

Togepi = Fairy('Togepi','175','Hada', '0.3m','1.5kg','H/M', 'Bolaclavos',5, 2, 3, 'Dicha', 'Luchador', 'Metal')

totodile = Water('Totodile', '158', 'Agua', '0.6m','9.5kg', 'H/M','Fauces', 5, 3,4,'Torrente', 'Fuego', 'Electricidad')

zapdos = Electric('Zapdos', '145', 'Electrico', '1.6m', '52.6kg','Desconocido', 'Electrico',8,4,5,'Presión', 'Agua', 'Suelo' )

#Funcion de pelea
def pelea():
    #Se crea la lista pokemon con los objetos pokemon dentro de ellas
    print ("Escoge dos pokemones para pelear")
    pokemons = {
                1: charizar,
                2: Mew,
                3: Togepi,
                4: totodile,
                5: zapdos 
                }
    #Se muestran las opciones a elegir
    for clave, valor in pokemons.items():
        print(f'{clave}: {valor.nombre}')
    #Se ingresa el primer pokemon a pelear
    player1 = int(input('Pokemon 1: '))
    #Se comprueba que sea una opción valida
    while (player1<0 or player1>5):
        player1 = int(input('Ingrese un valor válido para el pokemon 1 (1-5)'))
    #Se ingresa el segundo pokemon a pelear
    player2 = int(input('Pokemon 2: '))
    #Se comprueba que sea una opción valida
    while (player2<0 or player2>5):
        player2 = int(input('Ingrese un valor válido para el pokemon 1 (1-5)'))
    #inicia la pelea
    print(f'Pelea entre {pokemons[player1].nombre} y {pokemons[player2].nombre}' )
    #La vida de los pokemones se multiplica por 10, pues en las estadísticas usamos valores de unidad como venpia en la pokedex oficial de pokemon
    pokemons[player1].hp = pokemons[player1].hp*10
    pokemons[player2].hp = pokemons[player2].hp*10
    #Variable para cambiar de turno de pokemon
    i = 0
    while (pokemons[player1].hp>0 and pokemons[player2].hp>0):
        golpe =  randint(1,5)
        #Si es multiplo de 2 atacará el pokemon 1
        if(i%2==0):
            print(" ")
            #Si la debilidad del pokemon 2 es el tipo del pokemon 1 se le sumara 3 siempre a su ataque y siempre usara su habilidad especial
            if (pokemons[player1].fortaleza == pokemons[player2].tipo):
                golpe += 3
                print (pokemons[player1].nombre + " Uso " +pokemons[player1].habilidad)
                pokemons[player2].hp = pokemons[player2].hp - golpecle
                print (pokemons[player2].nombre + " le quedan " + str(pokemons[player2].hp) + " de vida ")
            #Si no es debilidad pero es un tiro mayor a 3 es un golpe crítico
            elif(golpe == 4 or golpe == 5):
                print ("Es un golpe crítico!!! " + pokemons[player1].nombre + " Uso " +pokemons[player1].habilidad)
                pokemons[player2].hp = pokemons[player2].hp - golpe
                print (pokemons[player2].nombre + " le quedan " + str(pokemons[player2].hp) + " de vida ")
            #Si es de 3 para abajo se hará un ataque normal
            else:
                print (pokemons[player1].nombre + " Uso ataque normal ")
                pokemons[player2].hp = pokemons[player2].hp - golpe
                print (pokemons[player2].nombre + " le quedan " + str(pokemons[player2].hp) + " de vida ")

        else:
            print(" ")
            #Si la debilidad del pokemon 1 es el tipo del pokemon 2 se le sumara 3 siempre a su ataque y siempre usara su habilidad especial
            if (pokemons[player2].fortaleza == pokemons[player1].tipo):
                golpe += 3
                print (pokemons[player2].nombre + " Uso " +pokemons[player2].habilidad)
                pokemons[player1].hp = pokemons[player1].hp - golpe
                print (pokemons[player1].nombre + " le quedan " + str(pokemons[player1].hp) + " de vida ")
            #Si no es debilidad pero es un tiro mayor a 3 es un golpe crítico
            elif(golpe == 4 or golpe == 5):
                print ("Es un golpe crítico!!! " + pokemons[player2].nombre + " Uso " +pokemons[player2].habilidad)
                pokemons[player1].hp = pokemons[player1].hp - golpe
                print (pokemons[player1].nombre + " le quedan " + str(pokemons[player1].hp) + " de vida ")
            #Si es de 3 para abajo se hará un ataque normal
            else:
                print (pokemons[player2].nombre + " Uso ataque normal ")
                pokemons[player1].hp = pokemons[player1].hp - golpe
                print (pokemons[player1].nombre + " le quedan " + str(pokemons[player1].hp) + " de vida ")
        i+=1
    #Se declara gandor al pokemon 2 si el pokemon 1 baja de 0 de vida
    if(pokemons[player1].hp<=0):
        print(" ")
        print(pokemons[player2].nombre + " Gano el combate, ha ganado 100 pts de exp, mientras que " + pokemons[player1].nombre + " se queda unicamente con 50 pts de exp")
    #Se declara gandor al pokemon 1 si el pokemon 2 baja de 0 de vida
    elif(pokemons[player2].hp<=0):
        print(" ")
        print(pokemons[player1].nombre + " Gano el combate, ha ganado 100 pts de exp, mientras que " + pokemons[player2].nombre + " se queda unicamente con 50 pts de exp")

