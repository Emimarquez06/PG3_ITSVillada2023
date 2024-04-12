def sumar_numeros():
    while True:
        try:
            numero1 = int(input("Ingresa tu primer número entero: "))
            numero2 = int(input("Ingresa tu segundo número entero: "))
            suma = numero1 + numero2
            print("La suma de sus números es:", suma)
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")
        finally:
            seguir = input("¿Queres seguir sumando valores? (Si/No): ").lower()
            if seguir != 'Si':
                break

sumar_numeros()
