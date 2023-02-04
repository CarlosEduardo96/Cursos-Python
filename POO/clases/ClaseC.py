class ClaseC:    
    @staticmethod
    def metodostatico():
        return "metodo estatico"

mi_clase= ClaseC()
print(ClaseC.metodostatico())
print(mi_clase.metodostatico)