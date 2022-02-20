#Función para imrimir la gráfica de Togepi
def Togepi_graf():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    #Atributos que se mostraran en la gráfica
    estadisticas = ["HP", "Ataque", "Defensa", "Atq Esp", "Def Esp", "Velocidad"]
    Togepi= {"Togepi": [3, 2, 4, 3, 4, 2]}
    #Se opta por una gráfica de barras
    ax.bar(estadisticas, Togepi["Togepi"], color = "#EDA6E8")
    #set_xlabel
    #set_ylabel
    ax.set_xlabel("Estadísticas", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#EDA6E8" })
    ax.set_ylabel("Puntos", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#EDA6E8" })
    #set_xlim
    #set_ylim
    ax.set_ylim([0, 10])
    #set_xticks
    #set_yticks
    ax.set_yticks(range(0, 10))
    #ax.legend
    ax.legend(["Togepi"], loc = "upper right")
    #Titulo de la grafica
    ax.set_title("Estadisticas Togepi", loc="center", fontdict = {"fontsize":20, "fontweight":"bold", "color": "#EDA6E8" })
    plt.show()