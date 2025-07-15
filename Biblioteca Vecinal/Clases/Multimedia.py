from Material import Material

class Multimedia(Material):
    def __init__(self, titulo, anio, autor, tipo, duracion):
        super().__init__(titulo, anio, autor)
        self.tipo = tipo
        self.duracion = duracion

    def getTipo(self):
        return self.tipo
    
    def getDuracion(self):
        return self.duracion