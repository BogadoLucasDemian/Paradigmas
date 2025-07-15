# Clase compuesta: crear, agregar, eliminar, recuperar, verTodos, existe, esVacia, tamanio

class Biblioteca:
    def __init__(self, nombre, direccion, barrio, responsable, horaApertura, horaCierre):
        self.nombre = nombre
        self.direccion = direccion
        self.barrio = barrio
        self.responsable = responsable
        self.horaApertura = horaApertura
        self.horaCierre = horaCierre
        self.usuarios = []
        self.materiales = []

    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getBarrio(self):
        return self.barrio
    
    def getResponsable(self):
        return self.responsable
    
    def getHoraApertura(self):
        return self.horaApertura
    
    def getHoraCierre(self):
        return self.horaCierre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setBarrio(self, barrio):
        self.barrio = barrio

    def setResponsable(self, responsable):
        self.responsable = responsable

    def setHoraApertura(self, horaApertura):
        self.horaApertura = horaApertura

    def setHoraCierre(self, horaCierre):
        self.horaCierre = horaCierre
    
    def agregarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def eliminarUsuario(self, usuario):
        self.usuarios.remove(usuario)
    
    def recuperarUsuario(self, index):
        return self.usuarios[index]
    
    def verTodosUsuarios(self):
        return self.usuarios
    
    def existeUsuario(self, usuario):
        return usuario in self.usuarios
    
    def esVaciaUsuarios(self):
        return len(self.usuarios) == 0
    
    def tamanioUsuarios(self):
        return len(self.usuarios)   
    
    def agregarMaterial(self, material):
        self.materiales.append(material)

    def eliminarMaterial(self, material):
        self.materiales.remove(material)

    def recuperarMaterial(self, index):
        return self.materiales[index]
    
    def verTodosMateriales(self):
        return self.materiales
    
    def existeMaterial(self, material):
        return material in self.materiales
    
    def esVaciaMateriales(self):
        return len(self.materiales) == 0
    
    def tamanioMateriales(self):
        return len(self.materiales)