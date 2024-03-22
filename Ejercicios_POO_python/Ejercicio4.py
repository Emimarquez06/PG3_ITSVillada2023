class Operaciones:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.realizar_operaciones()

    def realizar_operaciones(self):
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        resultado = self.numero1 + self.numero2
        print(f"Suma: {resultado}")

    def resta(self):
        resultado = self.numero1 - self.numero2
        print(f"Resta: {resultado}")

    def multiplicacion(self):
        resultado = self.numero1 * self.numero2
        print(f"Multiplicación: {resultado}")

    def division(self):
        if self.numero2 != 0:
            resultado = self.numero1 / self.numero2
            print(f"División: {resultado}")
        else:
            print("No se puede dividir entre cero.")


numero1 = int(input("Ingresa tu primer número entero: "))
numero2 = int(input("Ingresa tu segundo número entero: "))


operaciones = Operaciones(numero1, numero2)
