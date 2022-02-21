from re import X
from sympy import false
from Zapdos_python import Zapdos_graf
from Togepi_python import Togepi_graf
from Totodile_python import Totodile_graf
from Charizard_python import Charizard_graf
from Mew_python import Mew_graf
from ClassJason import estadisticas

#Funcion para mostrar las gráficas y las estádisticas de los pokemones
def mostrar_gráficas():
    ciclo = True
    #El usuario escoge el pokemon del que se desea saber susestadisticas
    print("Seleccione el pokemon del cual desea saber sus estadisticas")
    pokemons = {
        1: "Zapdos",
        2: "Togepi",
        3: "Charizard",
        4: "Totodile",
        5: "Mew" 
     }
    for clave, valor in pokemons.items():
        print(f'{clave}: {valor}')
    while (ciclo):
        try: 
            #Se guarda el valor ingresado por el pokemon y segun este se muestra el pokemon
            graf = int(input(': '))
            #Se llaman las estadisticas del pokemon seleccionado
            estadisticas(graf)
            #Grafica de Zapdos
            if graf == 1:
                Zapdos_graf()
                ciclo = false
            #Grafica de Togepi
            elif graf == 2:
                Togepi_graf()
                ciclo = false
            #Grafica de Charizard
            elif graf == 3:
                Charizard_graf()
                ciclo = false
            #Grafica de Totodile
            elif graf == 4:
                Totodile_graf()
                ciclo = false
            #Grafica de Mew
            elif graf == 5:
                Mew_graf()
                ciclo = false
            #En caso de no poner una opcion valida
            else:
                raise ValueError
        #Se muestra el error del usuario
        except ValueError:
            print('Verifique su elecciión')
        