class Usuario:
    def __init__(self, nombreCompleto, dni, domicilio, telefono, estadoMembresia):
        self.nombreCompleto = nombreCompleto
        self.dni = dni
        self.domicilio = domicilio
        self.telefono = telefono
        self.estadoMembresia = estadoMembresia

    def getNombreCompleto(self):
        return self.nombreCompleto
    
    def getDni(self):
        return self.dni
    
    def getDomicilio(self):
        return self.domicilio
    
    def getTelefono(self):
        return self.telefono
    
    def getEstadoMembresia(self):
        return self.estadoMembresia
    
    def setNombreCompleto(self, nombreCompleto):
        self.nombreCompleto = nombreCompleto

    def setDni(self, dni):
        self.dni = dni

    def setDomicilio(self, domicilio):
        self.domicilio = domicilio

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setEstadoMembresia(self, estadoMembresia):
        self.estadoMembresia = estadoMembresia