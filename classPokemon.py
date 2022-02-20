import random
class Pokemon():
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria):
        self._nombre = nombre
        self._numero = numero
        self._tipo = tipo 
        self._altura = altura
        self._peso = peso
        self._sexo = sexo
        self._categoria = categoria
        

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
    
    def inflingeDaño(self):
            return random(1, self.ataque)
            
    def inflingeDaño(self, modificador ='Normal'):
        daño = 0
        if (modificador == 'ventaja'):
            daño = random(1, self.ataquesp)+random(1,10)
        elif (modificador == 'desventaja'):
            while daño <= 0:
                daño = random(1,self.ataque)-random(1,self.ataque-3)
            else: 
                daño = random(1, self.ataque)  
        return daño
            
    def recibeAtaque(self,daño):
        return self.hp-daño
    
    def pelea(player1, player2):
        print(f'pelea entre {player1.nombre} y {player2.nombre}')