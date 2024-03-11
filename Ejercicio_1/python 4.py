def ordenar_de_mayor_a_menor(lista):
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada
lista = [5, 2, 8, 1, 7]
lista_ordenada = ordenar_de_mayor_a_menor(lista)

print("Esta es su lista original:", lista)
print("Esta es su lista ordenada de mayor a menor:", lista_ordenada)
