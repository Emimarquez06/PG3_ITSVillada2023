class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print("Nombre:", self.nombre)

#
persona1 = Persona("Juan")
persona2 = Persona("María")

persona1.mostrar_nombre()
persona2.mostrar_nombre()
