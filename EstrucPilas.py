class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.elementos = []
        self.tope = 0 

    def insertar(self, valor):
        if self.tope < self.capacidad:
            self.elementos.append(valor)
            self.tope += 1
            print(f"Insertar({valor}): Pila = {self.elementos}, TOPE = {self.tope}")
        else:
            print(f"Error: Desbordamiento al intentar insertar {valor}. TOPE = {self.tope}")

    def eliminar(self):
        if self.tope > 0:
            valor = self.elementos.pop()
            self.tope -= 1
            print(f"Eliminar({valor}): Pila = {self.elementos}, TOPE = {self.tope}")
            return valor
        else:
            print(f"Error: Subdesbordamiento. La pila está vacía, TOPE = {self.tope}")
            return None

pila = Pila(capacidad=8)

pila.insertar("X")   
pila.insertar("Y")   
pila.eliminar()      
pila.eliminar()      
pila.eliminar()      
pila.insertar("V")   
pila.insertar("W")   
pila.eliminar()      
pila.insertar("R")   

print(f"\nEstado final de la pila: {pila.elementos}, TOPE = {pila.tope}")
print(f"Número de elementos en la pila: {pila.tope}")
