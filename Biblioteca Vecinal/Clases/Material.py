class Material:
    codInventarioCounter = 1

    def __init__(self, codInventario, titulo, anioPublicacion, autor):
        self.codInventario = Material.codInventarioCounter
        Material.codInventarioCounter += 1
        self.titulo = titulo
        self.anioPublicacion = anioPublicacion
        self.autor = autor
        self.disponible = True

    def getCodInventario(self):
        return self.codInventario
    
    def getTitulo(self):
        return self.titulo
    
    def getAnioPublicacion(self):
        return self.anioPublicacion
    
    def getAutor(self):
        return self.autor
    
    def isDisponible(self):
        return self.disponible
    
    def setCodInventario(self, codInventario):
        self.codInventario = codInventario

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setAnioPublicacion(self, anioPublicacion):
        self.anioPublicacion = anioPublicacion

    def setAutor(self, autor):
        self.autor = autor

    def setDisponible(self, disponible):
        self.disponible = disponible