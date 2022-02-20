#Funcion para imprimir gráfica de Mew
def Mew_graf():   
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    #Atributos que se mostrarán
    estadisticas = ["HP", "Ataque", "Defensa", "Atq Esp", "Def Esp", "Velocidad"]
    Mew= {"Mew": [6, 6, 6, 6, 6, 6]}
    #Se opta por gráfica de tablas
    ax.bar(estadisticas, Mew["Mew"], color = "#F30AE3")
    #set_xlabel
    #set_ylabel
    ax.set_xlabel("Estadísticas", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#F30AE3" })
    ax.set_ylabel("Puntos", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#F30AE3" })
    #set_xlim
    #set_ylim
    ax.set_ylim([0, 10])
    #set_xticks
    #set_yticks
    ax.set_yticks(range(0, 10))
    #ax.legend
    ax.legend(["Mew"], loc = "upper right")
    #Titulo de la grafica
    ax.set_title("Mew", loc="center", fontdict = {"fontsize":20, "fontweight":"bold", "color": "#F30AE3" })
    plt.show()