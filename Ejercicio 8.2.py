import math
import tkinter as tk
from tkinter import messagebox


class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion_estandar(self):
        prom = self.calcular_promedio()
        return math.sqrt(sum((x - prom) ** 2 for x in self.lista_notas) / len(self.lista_notas))

    def calcular_mayor(self):
        return max(self.lista_notas)

    def calcular_menor(self):
        return min(self.lista_notas)


# interfaz
class VentanaNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("300x380")
        self.resizable(False, False)

        self._crear_componentes()

    def _crear_componentes(self):
        self.entradas_notas = []
        for i in range(5):
            tk.Label(self, text=f"Nota {i+1}:").place(x=20, y=20 + i*30, width=80, height=23)
            ent = tk.Entry(self)
            ent.place(x=110, y=20 + i*30, width=150, height=23)
            self.entradas_notas.append(ent)

        tk.Button(self, text="Calcular", command=self._calcular).place(x=30, y=180, width=100, height=25)
        tk.Button(self, text="Limpiar", command=self._limpiar).place(x=150, y=180, width=100, height=25)

        self.lbl_promedio = tk.Label(self, text="Promedio = ", anchor="w")
        self.lbl_promedio.place(x=20, y=220, width=250, height=23)

        self.lbl_desviacion = tk.Label(self, text="Desviación estándar = ", anchor="w")
        self.lbl_desviacion.place(x=20, y=250, width=250, height=23)

        self.lbl_mayor = tk.Label(self, text="Nota mayor = ", anchor="w")
        self.lbl_mayor.place(x=20, y=280, width=250, height=23)

        self.lbl_menor = tk.Label(self, text="Nota menor = ", anchor="w")
        self.lbl_menor.place(x=20, y=310, width=250, height=23)

    def _calcular(self):
        notas = Notas()

       
        for i, ent in enumerate(self.entradas_notas):
            texto = ent.get().strip()
            if texto == "":
                messagebox.showwarning("Alerta", f"Es obligatorio ingresar las cinco notas.\nFalta ingresar la Nota {i+1}.")
                return

        
        for i, ent in enumerate(self.entradas_notas):
            texto = ent.get().strip()
            try:
                valor = float(texto)
                notas.lista_notas[i] = valor
            except ValueError:
                messagebox.showerror("Error", f"Los datos deben ser valores numéricos.")
                return

        
        self.lbl_promedio.config(text=f"Promedio = {notas.calcular_promedio():.2f}")
        self.lbl_desviacion.config(text=f"Desviación estándar = {notas.calcular_desviacion_estandar():.2f}")
        self.lbl_mayor.config(text=f"Valor mayor = {notas.calcular_mayor():.2f}")
        self.lbl_menor.config(text=f"Valor menor = {notas.calcular_menor():.2f}")

    def _limpiar(self):
        for ent in self.entradas_notas:
            ent.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación estándar = ")
        self.lbl_mayor.config(text="Valor mayor = ")
        self.lbl_menor.config(text="Valor menor = ")


if __name__ == "__main__":
    VentanaNotas().mainloop()


    #ESTE Si    