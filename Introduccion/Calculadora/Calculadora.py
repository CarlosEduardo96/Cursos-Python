class Calculadora:
    def __init__(self, numero1, numero2):
        self._numero1=numero1
        self._numero2=numero2

    @property
    def Suma(self):
        return self._numero1+self._numero2
    
    @property
    def Resta(self):
        return self._numero1-self._numero2
    
    @property
    def Divicion(self):
        return self._numero1/self._numero2
