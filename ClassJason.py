import pandas as pd
def estadisticas(i):
    i-=1
    df = {'Nombre':['Zapdos', 'Togepi', 'Charizard', 'Totodile', 'Mew'], 'Numero':['145', '175', '6', '158', '151'], 'Tipo':['Eléctrico', 'Hada', 'Fuego', 'Agua', 'Psiquico'], 'altura':['1.6', '0.3', '1.7', '0.6', '0.4'], 'Peso':['52.6', '1.5', '92', '9.5', '4'], 'Sexo':['Femenino', 'Femenino', 'Masculino', 'Masculino', 'Desconocido'], 'Habilidad':['Presion', 'Entusiasmo', 'Mar llamas', 'Torrente', 'Sincronía']}
    df = pd.DataFrame(df)
    nombres = list(df["Nombre"])
    numero = list(df["Numero"])
    tipo = list(df["Tipo"])
    altura = list(df["altura"])
    peso = list(df["Peso"])
    sexo = list(df["Sexo"])
    habilidad = list(df["Habilidad"])
    print("Nombre: {}\nNumero: {}\nTipo: {}\nAltura: {}\nPeso: {}\nSexo: {}\nHabilidad: {}\n".format(nombres[i], numero[i], tipo[i], altura[i], peso[i], sexo[i], habilidad[i]))
    print("\n")