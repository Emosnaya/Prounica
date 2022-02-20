from random import randint
from classPokemon import Pokemon
#Se define la clase de los tipo fuego y heredan de pokemon
class Fire(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo fuego
        self.fortaleza = 'Bueno contra Acero, Bicho, Hielo, Planta'
        self.debilidad = 'Débil contra Agua, Dragón, Fuego, Roca'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo electrico y heredan de pokemon
class Electric(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo electrico
        self.fortaleza = 'Bueno contra Agua y Volador'
        self.debilidad = 'Débil contra Tierra, Dragon, Electrico y Planta'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo volador y heredan de pokemon
class Fly(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo volador
        self.fortaleza = 'Bueno contra Bicho, Lucha, Planta'
        self.debilidad = 'Débil contra Hielo, Roca y Electrico'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo hielo y heredan de pokemon
class Ice(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo hielo
        self.fortaleza = 'Bueno contra Dragón, Planta, Tierra y Volador'
        self.debilidad = 'Débil contra Acero, Agua, Fuego y Hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo piedra y heredan de pokemon
class Rock(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo piedra
        self.fortaleza = 'Bueno contra Bicho, Fuego, Hielo y Volador'
        self.debilidad = 'Débil contra Acero, Lucha y Tierra'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo piso y heredan de pokemon
class Ground(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo piso
        self.fortaleza = 'Bueno contra Acero, Electrico, Fuego, Roca y Veneno'
        self.debilidad = 'Débil contra Bicho, Planta y Volador'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo metal y heredan de pokemon
class Steel(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo metal
        self.fortaleza = 'Bueno contra Hielo, Hada y Roca'
        self.debilidad = 'Débil contra Acero, Eléctrico, Agua y Fuego'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo normal y heredan de pokemon
class Normal(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo normal
        self.fortaleza = 'Bueno contra Ninguno'
        self.debilidad = 'Débil contra Acero, Fantasma, Roca'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo bicho y heredan de pokemon
class Bug(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo bicho
        self.fortaleza = 'Bueno contra Planta, Psíquico, Siniestro'
        self.debilidad = 'Débil contra Acero, Fantasma, Fuego, Hada, Lucha, Volador, Veneno'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad