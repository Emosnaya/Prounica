from classPokemon import Pokemon

class Water(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, fortaleza, debilidad, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Fuego, Roca, Tierra'
        self.debilida = 'Débil contra Agua, Dragón, Planta'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


class Plant(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, fortaleza, debilidad, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Agua, Roca, Tierra'
        self.debilidad = 'Débil contra Acero, Bicho, Dragón, Fuego, Planta, Veneno, Volador'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad



class Poison(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, fortaleza, debilidad, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Hada, Planta'
        self.debilida = 'Débil contra Acero, Fantasma, Roca, Tierra, Veneno'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


class Fairy(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, fortaleza, debilidad, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Dragón, Lucha, Siniestro'
        self.debilida = 'Débil contra Acero, Fuego, Veneno'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


class Dragon(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, fortaleza, debilidad, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Dragón'
        self.debilida = 'Débil contra Acero, Hada'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


class Dark(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, fortaleza, debilidad, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Fantasma, Psíquico'
        self.debilida = 'Débil contra Hada, Lucha, Siniestro'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


class Fighter(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, fortaleza, debilidad, ataque, ataquesp, habilidad,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Normal'
        self.debilida = 'Débil contra Bicho, Fantasma, Hada, Psíquico, Veneno, Volador'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


class Ghost(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, fortaleza, debilidad, ataque, ataquesp, habilidad,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Fantasma, Volador'
        self.debilida = 'Débil contra Normal, Siniestro'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


class Psychic(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, fortaleza, debilidad, ataque, ataquesp, habilidad,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Lucha, Veneno'
        self.debilida = 'Débil contra Acero, Psíquico, Siniestro'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad
