#Se obtiene pandas para poder crear el data frames
import pandas as pd
#Funcion para crear el data frame con los valores de los pokemones, se usa la variable i como parametro que dara el usuario
def estadisticas(i):
    #Se le resta 1 a i para que coincida con los indices
    i-=1
    df = {'Nombre':['Zapdos', 'Togepi', 'Charizard', 'Totodile', 'Mew'], 'Numero':['145', '175', '6', '158', '151'], 'Tipo':['Eléctrico', 'Hada', 'Fuego', 'Agua', 'Psiquico'], 'altura':['1.6', '0.3', '1.7', '0.6', '0.4'], 'Peso':['52.6', '1.5', '92', '9.5', '4'], 'Sexo':['Femenino', 'Femenino', 'Masculino', 'Masculino', 'Desconocido'], 'Habilidad':['Presion', 'Entusiasmo', 'Mar llamas', 'Torrente', 'Sincronía']}
    df = pd.DataFrame(df)
    #Se almacenan en diccionarios para un uso mas sencillo y poder llamarlos según pida el usuario
    nombres = list(df["Nombre"])
    numero = list(df["Numero"])
    tipo = list(df["Tipo"])
    altura = list(df["altura"])
    peso = list(df["Peso"])
    sexo = list(df["Sexo"])
    habilidad = list(df["Habilidad"])
    #Se imprimen los valores correspondientes con el indice solicitado por el usuario
    print("Nombre: {}\nNumero: {}\nTipo: {}\nAltura: {}\nPeso: {}\nSexo: {}\nHabilidad: {}\n".format(nombres[i], numero[i], tipo[i], altura[i], peso[i], sexo[i], habilidad[i]))
    print("\n")