import random
#Se decalara una clase global que heredarán las demás clases
class Pokemon():
    def __init__(self, nombre, numero, tipo, altura, peso, sexo, categoria):
        #declaración de atributos
        self._nombre = nombre
        self._numero = numero
        self._tipo = tipo 
        self._altura = altura
        self._peso = peso
        self._sexo = sexo
        self._categoria = categoria
        
    #Las propiedades de la clase  principal se hacen privadas y usamos el setter para definir los atributos
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
    