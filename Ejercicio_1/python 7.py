def es_numero_step(numero):
    str_numero = str(numero)
    
    for i in range(len(str_numero) - 1):
        if abs(int(str_numero[i]) - int(str_numero[i + 1])) != 1:
            return False
    
    return True
numero_usuario = int(input("Por favor ingresa un número para verificar si es un número 'step': "))

if es_numero_step(numero_usuario):
    print(f"{numero_usuario} es un número 'step'.")
else:
    print(f"{numero_usuario} no es un número 'step'.")
