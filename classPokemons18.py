from random import randint
from classPokemon import Pokemon
#Se define la clase de los tipo fuego y heredan de pokemon
class Fire(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad
    

class Electric(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
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
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad