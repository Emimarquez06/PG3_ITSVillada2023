def realizar_division():
    while True:
        try:
            numero1 = float(input("Ingresa tu primer número: "))
            numero2 = float(input("Ingresa tu segundo número: "))
            resultado = numero1 / numero2
            print("El resultado de la división que pediste es:", resultado)
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero. Por favor, ingresa un segundo número que no sea cero.")
        except ValueError:
            print("Error: Por favor, ingresa valores numéricos válidos.")
        else:
            break

realizar_division()
