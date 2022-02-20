from ClassJason import DataFrame

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
        pokemones = DataFrame()
        pokemones.df
        #print 
    elif opcion == 2:
        print ("Escoge dos pokemones para pelear")
    elif opcion == 3:
        salir = True
        print("RECUERDA TRATAR CON AMOR TUS POKEMONES")
    else:
        print ("Introduce un numero entre 1 y 3")

print ("Fin")