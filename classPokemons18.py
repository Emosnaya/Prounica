from classPokemon import Pokemon

class Fire(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp,):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp

class Electric(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad)
    

class Fly(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad)


class Ice(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad)

class Rock(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad)


class Ground(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad)

class Steel(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad)

class Normal(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad)

class Bug(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria, habilidad, ps, ataque, defensa, ataqueEsp, defensaEsp, velocidad, debilidad)