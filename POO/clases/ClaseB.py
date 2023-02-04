class ClaseA:
    def metodo(self, arg1, arg2):
        return "metodo normal", self
    
mi_clase= ClaseB()
print(mi_clase.metodo("a", "b"))

#Puedes acceder y modificar atributos
#Puedes acceder a otros metodos
#Dado que tiene el objeto self pudes acceder self.class, se modifica el estado de la clase

class ClaseB:
    @classmethod
    def metododeclase(cls):
        return "metodo de clase ",cls

#Laamado 1
ClaseB.metododeclase()

#Llamado 2
mi_claseb= ClaseB()
mi_claseb.metododeclase()

## No puedes acceder a los atributos de la instancia del objeto

