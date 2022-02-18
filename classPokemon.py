from random import randint


class Pokemon():
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria, hp, ataque, ataquesp):
        self._nombre = nombre
        self._numero = numero
        self._tipo = tipo 
        self._altura = altura
        self._peso = peso
        self._sexo = sexo
        self._categoria = categoria
        self.hp = hp
        self.ataque = ataque
        self.ataquesp = ataquesp
    
        

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numerp(self, numero):
        self._numero = numero
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self,altura):
        self._altura = altura
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, peso):
        self._peso = peso
    
    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo
    
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria
    
    @property
    def habilidad(self):
        return self._habilidad
    
    @habilidad.setter
    def habilidad(self, habilidad):
        self._habilidad = habilidad


    def archivos():
        pass
    
    def inflingeDaño(self):
        return randint(1, self.ataque)

    def inflingeDaño(self, modificador ='Normal'):
        daño = 0
        if (modificador == 'ventaja'):
            daño = randint(1, self.ataquesp)+randint(1,5)
        elif (modificador == 'desventaja'):
            while daño <= 0:
                daño = randint(1,self.ataque)-randint(1,self.ataque-1)
        else: 
            daño = randint(1, self.ataque)
        
        return daño
    
    def recibeAtaque(self,daño):
        return self.hp-daño

