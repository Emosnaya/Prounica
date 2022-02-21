#def estadisticas():
import json
import pandas as pd
data = './pokemones.json'

with open(data) as file:
    data = json.load(file)
    for Nombre in data.items():
        print("HP")
