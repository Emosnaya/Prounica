from random import randint
from classPokemon import Pokemon

class Fire(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
    
    def inflingeDaño(self):
        return randint(1, self.ataque)
    
    def inflingeDaño(self, modificador ='Normal'):
        daño = 0
        if (modificador == 'ventaja'):
            daño = randint(1, self.ataquesp)+randint(1,10)
        elif (modificador == 'desventaja'):
            while daño <= 0:
                daño = randint(1,self.ataque)-randint(1,self.ataque-3)
        else: 
            daño = randint(1, self.ataque)
        
        return daño
    
    def recibeAtaque(self,daño):
        self.hp-daño
    


    


    


class Electric(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp

class Fly(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp

class Ice(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp

class Rock(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp

class Ground(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp

class Steel(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp

class Normal(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp

class Bug(Pokemon):
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        super().__init__(nombre, numero, tipo, altura, peso, sexo, categoria)
        self.habilidad = 'Bueno contra Hielo'
        self.debilida = 'Débil contra hielo'
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp