from Material import Material

class Revista(Material):
    def __init__(self, titulo, anio, autor, nro_edicion, periodicidad):
        super().__init__(titulo, anio, autor)
        self.nro_edicion = nro_edicion
        self.periodicidad = periodicidad

    def getNroEdicion(self):
        return self.nro_edicion
    
    def getPeriodicidad(self):
        return self.periodicidad
    
    def setNroEdicion(self, nro_edicion):
        self.nro_edicion = nro_edicion

    def setPeriodicidad(self, periodicidad):
        self.periodicidad = periodicidad

