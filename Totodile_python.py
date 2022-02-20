#Función para imprimir la gráfica de Charizard
def Totodile_graf():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    #Atributos que se mostraran en la tabla
    estadisticas = ["HP", "Ataque", "Defensa", "Atq Esp", "Def Esp", "Velocidad"]
    Totodile= {"Totodile": [3, 3, 4, 3, 3, 3]}
    #Se opta por una tabla de barras
    ax.bar(estadisticas, Totodile["Totodile"], color = "#22C4DE")
    #set_xlabel
    #set_ylabel
    ax.set_xlabel("Estadísticas", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#22C4DE" })
    ax.set_ylabel("Puntos", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#22C4DE" })
    #set_xlim
    #set_ylim
    ax.set_ylim([0, 10])
    #set_xticks
    #set_yticks
    ax.set_yticks(range(0, 10))
    #ax.legend
    ax.legend(["Totodile"], loc = "upper right")
    ax.set_title("Totodile", loc="center", fontdict = {"fontsize":20, "fontweight":"bold", "color": "#22C4DE" })
    while True:
        plt.show()