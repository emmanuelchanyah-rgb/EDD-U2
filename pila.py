class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)
        print(f"Se apiló: {item}")

    def desapilar(self):
        if not self.esta_vacia():
            elemento = self.items.pop()
            print(f"Se desapiló: {elemento}")
        else:
            print("La pila está vacía, no se puede desapilar.")

    def ver_tope(self):
        if not self.esta_vacia():
            print(f"El tope de la pila es: {self.items[-1]}")
        else:
            print("La pila está vacía.")

    def mostrar(self):
        if not self.esta_vacia():
            print("Pila actual:", self.items)
        else:
            print("La pila está vacía.")


if __name__ == "__main__":
    pila = Pila()

    while True:
        print("\n MENÚ PILA ")
        print("1. Apilar (Push)")
        print("2. Desapilar (Pop)")
        print("3. Ver tope (Peek)")
        print("4. Mostrar pila")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dato = input("Ingresa un elemento para apilar: ")
            pila.apilar(dato)
        elif opcion == "2":
            pila.desapilar()
        elif opcion == "3":
            pila.ver_tope()
        elif opcion == "4":
            pila.mostrar()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
