def dibujar_rectangulo(ancho, alto, caracter):
    for i in range(alto):
        fila = caracter * ancho
        print(fila)

def main():
    try:
        
        ancho = int(input("Por favor ingresa el ancho del rectángulo: "))
        alto = int(input("Por favor ingresa el alto del rectángulo: "))
        caracter = input("Por favor ingresa el caracter para el dibujo: ")

        
        dibujar_rectangulo(ancho, alto, caracter)
    except ValueError:
        print("Por favor, ingrese valores numéricos para el ancho y el alto.")

if __name__ == "__main__":
    main()
