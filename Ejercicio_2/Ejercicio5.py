class Persona:
    def __init__(self, nom, edad):
        self.nom = nom
        self.edad = edad

    def cargar(self):
        self.nom= input("Ingresa tu nombre: \n>>>")
        self.edad = int(input("Ingresa tu edad: \n>>>"))

    def imprimir(self):
        print(f" Su nombre es: {self.nom} \nSu edad es: {self.edad}")


class Empleado(Persona):
    def __init__(self, sueldo, nom, edad):
        super().__init__(nom, edad)
        self.sueldo = sueldo

    def impuesto(self):
        if self.sueldo > 3000:
            print(f"Usted {self.nom}, si paga impuestos")
        else:
            print("Usted no paga impuestos")


persona1 = Persona("", 0)
persona1.cargar()
persona1.imprimir()

empleado1 = Empleado(3100,"Lionel", 36)
empleado1.impuesto()
empleado1.imprimir()