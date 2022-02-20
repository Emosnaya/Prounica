from re import X
from Zapdos_python import Zapdos_graf
from Togepi_python import Togepi_graf
from Totodile_python import Totodile_graf
from Charizard_python import Charizard_graf
from Mew_python import Mew_graf

def mostrar_gráficas():
    print ("Seleccione el pokemon del cual desea saber sus estadisticas")
    pokemons = {
        1: "Charizard",
        2: "Mew",
        3: "Togepi",
        4: "Totodile",
        5: "Zapdos" 
     }
    for clave, valor in pokemons.items():
        print(f'{clave}: {valor}')
    try: 
        graf = int(input(': '))

        if graf == 1:
            Charizard_graf()
        elif graf == 2:
            Mew_graf()
        elif graf == 3:
            Togepi_graf()
        elif graf == 4:
            Totodile_graf()
        elif graf == 5:
            Zapdos_graf()
        else:
            raise ValueError
    except ValueError:
        print('Verifique su elecciión')
        