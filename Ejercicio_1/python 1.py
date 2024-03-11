lista = [10, 20, 30, 40, 50, 60, 70]
def buscar_valor(lista, elemento):
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return None

elemento_buscado = int(input("Por favor ingresa el valor que desea buscar en la lista: "))

indice_encontrado = buscar_valor(lista, elemento_buscado)

if indice_encontrado is not None:
    print("El elemento {elemento_buscado} se encuentra en la posición {indice_encontrado} de la lista.")
else:
    print("El elemento {elemento_buscado} no se encuentra en la lista.")


