from re import X

from sympy import false
from DataFrame import df
from Zapdos_python import Zapdos_graf
from Togepi_python import Togepi_graf
from Totodile_python import Totodile_graf
from Charizard_python import Charizard_graf
from Mew_python import Mew_graf
from ClassJason import estadisticas

def mostrar_gráficas():
    ciclo = True
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
            graf = int(input(': '))
            estadisticas(graf)
            if graf == 1:
                Zapdos_graf()
                ciclo = false
            elif graf == 2:
                Togepi_graf()
                ciclo = false
            elif graf == 3:
                Charizard_graf()
                ciclo = false
            elif graf == 4:
                Totodile_graf()
                ciclo = false
            elif graf == 5:
                Mew_graf()
                ciclo = false
            else:
                raise ValueError
        except ValueError:
            print('Verifique su elecciión')
        