import tkinter as tk
from tkinter import messagebox

class PilaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pila con Interfaz Gráfica")


        self.items = []

    
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)

      
        botones_frame = tk.Frame(root)
        botones_frame.pack()

        tk.Button(botones_frame, text="Apilar", width=10, command=self.apilar).grid(row=0, column=0, padx=5)
        tk.Button(botones_frame, text="Desapilar", width=10, command=self.desapilar).grid(row=0, column=1, padx=5)
        tk.Button(botones_frame, text="Ver cima", width=10, command=self.ver_cima).grid(row=0, column=2, padx=5)

        
        self.frame_pila = tk.Frame(root, bg="white", bd=2, relief="solid", height=300, width=200)
        self.frame_pila.pack(pady=10)

       
        self.label_estado = tk.Label(root, text=" Pila vacía", font=("Arial", 12, "bold"))
        self.label_estado.pack()

        self.frame_pila.pack_propagate(False)

    def apilar(self):
        elemento = self.entry.get()
        if elemento:
            self.items.append(elemento)
            self.entry.delete(0, tk.END)
            self.actualizar_pila()
        else:
            messagebox.showwarning("Advertencia", "Debes ingresar un valor")

    def desapilar(self):
        if self.items:
            eliminado = self.items.pop()
            messagebox.showinfo("Desapilado", f"Se desapiló: {eliminado}")
            self.actualizar_pila()
        else:
            messagebox.showwarning("Advertencia", "La pila está vacía")

    def ver_cima(self):
        if self.items:
            messagebox.showinfo("Cima", f"Elemento en cima: {self.items[-1]}")
        else:
            messagebox.showwarning("Advertencia", "La pila está vacía")

    def actualizar_pila(self):
        for widget in self.frame_pila.winfo_children():
            widget.destroy()

        if not self.items:
            self.label_estado.config(text=" Pila vacía")
        else:
            self.label_estado.config(text=" Estado de la pila")

            for elemento in reversed(self.items):
                bloque = tk.Label(self.frame_pila, text=str(elemento),
                                  font=("Arial", 12), width=15, height=2,
                                  bg="lightblue", relief="solid", borderwidth=2)
                bloque.pack(pady=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = PilaGUI(root)
    root.mainloop()

