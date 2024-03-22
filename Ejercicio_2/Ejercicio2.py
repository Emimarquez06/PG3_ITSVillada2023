class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir_info(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
    
    def verificar_regularidad(self):
        if self.nota >= 4:
            print(f"{self.nombre} Está Regular.")
        else:
            print(f"{self.nombre} Está Libre.")


alumno1 = Alumno("Francisco", 9)
alumno2 = Alumno("Manuel", 3)


alumno1.imprimir_info()
alumno1.verificar_regularidad()

alumno2.imprimir_info()
alumno2.verificar_regularidad()
