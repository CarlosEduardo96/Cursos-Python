class Persona:
    def __init__(self):
        self._nombre=""
        self._apellidos=""

    @property
    def Nombre(self):
        return self._nombre

    @Nombre.setter
    def setNombre(self, nombre=None):
        self._nombre=nombre

    @property
    def Apellidos(self):
        return self._apellidos

    @Apellidos.setter
    def setApellidos(self, apellidos=None):
      self._apellidos=apellidos
