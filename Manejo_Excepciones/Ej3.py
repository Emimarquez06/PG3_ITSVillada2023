def mostrar_nombre_mes():
    meses_del_año = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                     'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    while True:
        try:
            numero_mes = int(input("Ingresa el número de mes (1-12): "))
            if 1 <= numero_mes <= 12:
                nombre_mes = meses_del_año[numero_mes - 1]
                print("El nombre del mes es:", nombre_mes)
            else:
                print("Error: Por favor, ingrese un número de un mes válido (1-12).")
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")
        except IndexError:
            print("Error: El número de mes ingresado está fuera del rango permitido (1-12).")

        seguir = input("¿Queres ingresar otro número de mes? (Si/No): ").lower()
        if seguir != 'Si':
            break

mostrar_nombre_mes()
