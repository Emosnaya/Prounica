from random import randint
from classPokemon import Pokemon
#Se define la clase de los tipo fuego y heredan de pokemon
class Fire(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo fuego
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo electrico y heredan de pokemon
class Electric(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo electrico
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo volador y heredan de pokemon
class Fly(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo volador
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo hielo y heredan de pokemon
class Ice(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo hielo
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo piedra y heredan de pokemon
class Rock(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo piedra
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo piso y heredan de pokemon
class Ground(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo piso
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo metal y heredan de pokemon
class Steel(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo metal
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo normal y heredan de pokemon
class Normal(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo normal
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo bicho y heredan de pokemon
class Bug(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los tipo bicho
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad