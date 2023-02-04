class Animal:
    def __init__(self, especie, edad):
        self._especie=especie
        self._edad=edad

    @property
    def getEspecie(self):
        return self._especie
    
    @getEspecie.setter
    def setEspecie(self, especie=None):
        self._especie=especie

    @property
    def getEdad(self):
        return self._edad
    
    @getEspecie.setter
    def setEdad(self, edad=None):
        self._edad=edad

    def hablar(seft):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("soy un animal de tipo ", type(self).__name__)
