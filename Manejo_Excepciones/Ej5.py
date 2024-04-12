try:
    with open("strings.txt", "w") as file:
        
        strings = ["Hola", "Mundo", "Python", "Emiliano"]
        for string in strings:
            file.write(string + "\n")  
        file.write(123) 
except TypeError as e:
    print("Error: Se esperaba un string pero se dió un entero.")
    print(e)
