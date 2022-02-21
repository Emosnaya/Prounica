from classPokemon import Pokemon
#Se define la clase de los tipo agua y hereda de pokemon
class Water(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones agua
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo planta y hereda de pokemon
class Plant(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones planta
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad


#Se define la clase de los tipo veneno y hereda de pokemon
class Poison(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones veneno
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo hada y hereda de pokemon
class Fairy(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones hada
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo dragon y hereda de pokemon
class Dragon(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones dragon
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo oscuro y hereda de pokemon
class Dark(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones siniestro
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo peleador y hereda de pokemon
class Fighter(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones peleadores
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo fantasma y hereda de pokemon
class Ghost(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad

#Se define la clase de los tipo psiquicos y hereda de pokemon
class Psychic(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp, habilidad, fortaleza, debilidad,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        #Fortalezas y debilidades de los pokemones psiquicos
        self.fortaleza = fortaleza
        self.debilidad = debilidad
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
        self.habilidad = habilidad
