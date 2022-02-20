import matplotlib.pyplot as plt
fig, ax = plt.subplots()
estadisticas = ["HP", "Ataque", "Defensa", "Atq Esp", "Def Esp", "Velocidad"]
Charizard= {"Charizard": [5, 5, 5, 7, 5, 6]}
ax.bar(estadisticas, Charizard["Charizard"], color = "#F13406")
#set_xlabel
#set_ylabel
ax.set_xlabel("Estadísticas", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#F13406" })
ax.set_ylabel("Puntos", fontdict = {"fontsize":14, "fontweight":"bold", "color": "#F13406" })
#set_xlim
#set_ylim
ax.set_ylim([0, 10])
#set_xticks
#set_yticks
ax.set_yticks(range(0, 10))
#ax.legend
ax.legend(["Charizard"], loc = "upper right")
ax.set_title("Charizard", loc="center", fontdict = {"fontsize":20, "fontweight":"bold", "color": "#F13406" })
plt.show()