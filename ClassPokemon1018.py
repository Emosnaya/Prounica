from classPokemon import Pokemon
#Se define la clase de los tipo agua y hereda de pokemon
class Water(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones agua
        self.fortaleza = 'Bueno contra Fuego, Roca, Tierra'
        self.debilidad = 'Débil contra Agua, Dragón, Planta'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo planta y hereda de pokemon
class Plant(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones planta
        self.fortaleza = 'Bueno contra Agua, Roca, Tierra'
        self.debilidad = 'Débil contra Acero, Bicho, Dragón, Fuego, Planta, Veneno, Volador'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


#Se define la clase de los tipo veneno y hereda de pokemon
class Poison(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones veneno
        self.fortaleza = 'Bueno contra Hada, Planta'
        self.debilidad = 'Débil contra Acero, Fantasma, Roca, Tierra, Veneno'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo hada y hereda de pokemon
class Fairy(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones hada
        self.fortaleza = 'Bueno contra Dragón, Lucha, Siniestro'
        self.debilidad = 'Débil contra Acero, Fuego, Veneno'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo dragon y hereda de pokemon
class Dragon(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones dragon
        self.fortaleza = 'Bueno contra Dragón'
        self.debilidad = 'Débil contra Acero, Hada'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo oscuro y hereda de pokemon
class Dark(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones siniestro
        self.fortaleza = 'Bueno contra Fantasma, Psíquico'
        self.debilidad = 'Débil contra Hada, Lucha, Siniestro'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo peleador y hereda de pokemon
class Fighter(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones peleadores
        self.fortaleza = 'Bueno contra Normal'
        self.debilidad = 'Débil contra Bicho, Fantasma, Hada, Psíquico, Veneno, Volador'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo fantasma y hereda de pokemon
class Ghost(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = 'Bueno contra Fantasma, Volador'
        self.debilidad = 'Débil contra Normal, Siniestro'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo psiquicos y hereda de pokemon
class Psychic(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones psiquicos
        self.fortaleza = 'Bueno contra Lucha, Veneno'
        self.debilidad = 'Débil contra Acero, Psíquico, Siniestro'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad
