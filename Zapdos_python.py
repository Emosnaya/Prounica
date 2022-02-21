#Funcion para imprimir la grafica de Zapdos
from typing_extensions import Self


def Zapdos_graf():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    #Atributos que se van a mostrar
    estadisticas = ["HP", "Ataque", "Defensa", "Atq Esp", "Def Esp", "Velocidad"]
    Zapdos= {"Zapdos": [6, 6, 5, 7, 6, 6]}
    #Se opta por grafica de barras
    ax.bar(estadisticas, Zapdos["Zapdos"], color = "#FADA0D")
    #set_xlabel
    #set_ylabel
    ax.set_xlabel("Estadísticas", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#FADA0D" })
    ax.set_ylabel("Puntos", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#FADA0D" })
    #set_xlim
    #set_ylim
    ax.set_ylim([0, 10])
    #set_xticks
    #set_yticks
    ax.set_yticks(range(0, 10))
    #ax.legend
    ax.legend(["Zapdos"], loc = "upper right")
    #Titulo de la grafica
    ax.set_title("Estadisticas Zapdos", loc="center", fontdict = {"fontsize":20, "fontweight":"bold", "color": "#FADA0D" })
    plt.show()

Zapdos_graf()