def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

palabra_usuario = input("Por favor ingresa una palabra para verificar si es un palíndromo: ")

if es_palindromo(palabra_usuario):
    print(f"{palabra_usuario} es un palíndromo.")
else:
    print(f"{palabra_usuario} no es un palíndromo.")
