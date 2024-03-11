def contar_vocales(frase):
    frase = frase.lower()
    cantidad_vocales = sum(1 for letra in frase if letra in 'aeiouáéíóúü')
    
    return cantidad_vocales

frase_usuario = input("Por favor ingresa una frase para contar las vocales: ")

cantidad_vocales = contar_vocales(frase_usuario)

print(f"La frase '{frase_usuario}' tiene {cantidad_vocales} vocal(es).")
