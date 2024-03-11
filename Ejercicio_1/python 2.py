def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        
        año = int(input("Por favor ingresa un año para verificar si el mismo es bisiesto: "))

       
        if es_bisiesto(año):
            print(f"¡El año {año} es bisiesto!")
        else:
            print(f"El año {año} no es bisiesto.")
    except ValueError:
        print("Por favor, ingrese un año válido.")

if __name__ == "__main__":
    main()
