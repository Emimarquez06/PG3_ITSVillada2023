def realizar_division():
    while True:
        try:
            numero1 = float(input("Ingresa tu primer número: "))
            numero2 = float(input("Ingresa tu segundo número: "))
            resultado = numero1 / numero2
            print("El resultado de tu división es:", resultado)
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero. Por favor, ingresa un segundo numero que no sea cero.")
        else:
            break

realizar_division()
