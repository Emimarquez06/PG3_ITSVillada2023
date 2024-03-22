class Familia:
    def __init__(self, nombre_padre, nombre_madre, hijos):
        self.nombre_padre = nombre_padre
        self.nombre_madre = nombre_madre
        self.hijos = hijos
    
    def __str__(self):
        hijos_str = ", ".join(self.hijos)
        return f"Padre: {self.nombre_padre}, Madre: {self.nombre_madre}, Hijos: {hijos_str}"


familia1 = Familia("Rodrigo", "Soledad", ["Emiliano", "LIsandro"])


print(familia1)
