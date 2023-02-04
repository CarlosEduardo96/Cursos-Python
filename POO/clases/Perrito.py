from Animal import Animal

class Perrito(Animal):
    def __init__(self):
        self._nombre=""
        self._raza=""

    @property
    def Nombre(self):
        return self._nombre
    
    @Nombre.setter
    def setNombre(self, nombre=None):
        self._nombre=nombre
    
    @property
    def Raza(self):
        return self._raza

    @Raza.setter
    def setRaza(self, raza=None):
        self._raza=raza




mi_perro= Perrito()
mi_perro.setNombre="budy"
mi_perro.setRaza="pug"

print(type(mi_perro))

print(mi_perro.Nombre, mi_perro.Raza)

mi_perro.describeme()