from Material import Material

class Libros(Material):
    def __init__(self, titulo, autor, anio, genero, paginas):
        super().__init__(titulo, autor, anio)
        self.genero = genero
        self.paginas = paginas
    
    def getGenero(self):
        return self.genero 
    
    def getPaginas(self):
        return self.paginas
    
    def setGenero(self, genero):
        self.genero = genero

    def setPaginas(self, paginas):
        self.paginas = paginas        