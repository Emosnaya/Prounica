from random import randint
from classPokemon import Pokemon

class Fire(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Acero, Bicho, Hielo, Planta'
        self.debilidad = 'Débil contra Agua, Dragón, Fuego, Roca'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


class Electric(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Agua y Volador'
        self.debilida = 'Débil contra Tierra, Dragon, Electrico y Planta'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

class Fly(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Bicho, Lucha, Planta'
        self.debilida = 'Débil contra Hielo, Roca y Electrico'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

class Ice(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Dragón, Planta, Tierra y Volador'
        self.debilida = 'Débil contra Acero, Agua, Fuego y Hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

class Rock(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Bicho, Fuego, Hielo y Volador'
        self.debilida = 'Débil contra Acero, Lucha y Tierra'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

class Ground(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Acero, Electrico, Fuego, Roca y Veneno'
        self.debilida = 'Débil contra Bicho, Planta y Volador'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

class Steel(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Hielo, Hada y Roca'
        self.debilida = 'Débil contra Acero, Eléctrico, Agua y Fuego'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

class Normal(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Ninguno'
        self.debilida = 'Débil contra Acero, Fantasma, Roca'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

class Bug(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Planta, Psíquico, Siniestro'
        self.debilida = 'Débil contra Acero, Fantasma, Fuego, Hada, Lucha, Volador, Veneno'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad