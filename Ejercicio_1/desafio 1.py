def dibujar_rectangulo(ancho, alto, caracter):
    for i in range(alto):
        fila = caracter * ancho
        print(fila)

def dibujar_triangulo(alto, caracter):
    for i in range(1, alto + 1):
        fila = caracter * i
        print(fila)

def main():
    try:
        ancho = int(input("Por favor ingresa el ancho de su rectángulo o triángulo: "))
        alto = int(input("Por favor ingresa el alto de su rectángulo o triángulo: "))
        caracter = input("Por favor ingresa el caracter para el dibujo: ")
        opcion = int(input("Por favor ingresa 1 para dibujar un rectángulo, 2 para dibujar un triángulo: "))

        if opcion == 1:
            dibujar_rectangulo(ancho, alto, caracter)
        elif opcion == 2:
            dibujar_triangulo(alto, caracter)
        else:
            print("Opción no válida. Por favor, ingrese solamente 1 o 2.")
    except ValueError:
        print("Por favor, ingrese los valores numéricos para el ancho y el alto.")

if __name__ == "__main__":
    main()
