class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def imprimir_lado_mayor(self):
        print("Lado mayor:", max(self.lado1, self.lado2, self.lado3))
    
    def equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")


def ingresar_lados():
    lado1 = float(input("Ingresa tu primer lado del triángulo: "))
    lado2 = float(input("Ingresa tu segundo lado del triángulo: "))
    lado3 = float(input("Ingresa tu tercer lado del triángulo: "))
    return lado1, lado2, lado3


lado1, lado2, lado3 = ingresar_lados()
triangulo = Triangulo(lado1, lado2, lado3)


triangulo.imprimir_lado_mayor()
triangulo.equilatero()
