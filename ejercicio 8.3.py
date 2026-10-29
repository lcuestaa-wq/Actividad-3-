import math
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    @abstractmethod
    def calcular_volumen(self): pass

    @abstractmethod
    def calcular_superficie(self): pass


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return math.pi * self.radio** 2 * self.altura

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (4.0 / 3.0) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        return 4.0 * math.pi * (self.radio ** 2)


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return ((self.base ** 2) * self.altura) / 3.0

    def calcular_superficie(self):
        return (self.base ** 2) + (2.0 * self.base * self.apotema)


class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return self.lado ** 3

    def calcular_superficie(self):
        return 6.0 * (self.lado ** 2)


class Prisma(FiguraGeometrica):
    def __init__(self, base, profundidad, altura):
        self.base = base
        self.profundidad = profundidad
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return self.base * self.profundidad * self.altura

    def calcular_superficie(self):
        return 2.0 * (self.base * self.profundidad + self.base * self.altura + self.profundidad * self.altura)


#imagenes
def agregar_imagen_figura(ventana, tipo_figura):
    """Muestra un dibujo de la figura seleccionada."""
    canvas = tk.Canvas(ventana, width=90, height=90, bg="#F0F0F0", highlightthickness=1)
    canvas.place(x=270, y=20)

    if tipo_figura == "cilindro":
        canvas.create_oval(20, 15, 70, 30, outline="black", width=2)
        canvas.create_line(20, 22, 20, 68, width=2)
        canvas.create_line(70, 22, 70, 68, width=2)
        canvas.create_oval(20, 55, 70, 75, outline="black", width=2)

    elif tipo_figura == "esfera":
        canvas.create_oval(15, 15, 75, 75, outline="black", width=2)
        canvas.create_oval(15, 38, 75, 52, outline="gray", dash=(3, 2))

    elif tipo_figura == "piramide":
        canvas.create_polygon(45, 15, 15, 75, 75, 75, outline="black", fill="", width=2)
        canvas.create_line(45, 15, 45, 75, fill="gray", dash=(3, 2))

    elif tipo_figura == "cubo":
        canvas.create_rectangle(15, 30, 60, 75, outline="black", width=2)
        canvas.create_rectangle(30, 15, 75, 60, outline="black", width=2)
        canvas.create_line(15, 30, 30, 15, width=2)
        canvas.create_line(60, 30, 75, 15, width=2)
        canvas.create_line(15, 75, 30, 60, width=2)
        canvas.create_line(60, 75, 75, 60, width=2)

    elif tipo_figura == "prisma":
        canvas.create_rectangle(15, 35, 55, 75, outline="black", width=2)
        canvas.create_rectangle(35, 15, 75, 55, outline="black", width=2)
        canvas.create_line(15, 35, 35, 15, width=2)
        canvas.create_line(55, 35, 75, 15, width=2)
        canvas.create_line(15, 75, 35, 55, width=2)
        canvas.create_line(55, 75, 75, 55, width=2)


# interfaces
class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("380x210")
        self.resizable(False, False)

        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.ent_radio = tk.Entry(self)
        self.ent_radio.place(x=110, y=20, width=135)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.ent_altura = tk.Entry(self)
        self.ent_altura.place(x=110, y=50, width=135)

        tk.Button(self, text="Calcular", command=self._calcular).place(x=110, y=80, width=135)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=120, width=240)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=150, width=240)

        agregar_imagen_figura(self, "cilindro")

    def _calcular(self):
        try:
            cil = Cilindro(float(self.ent_radio.get()), float(self.ent_altura.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {cil.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cil.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo vacío o formato numérico no válido")


class VentanaEsfera(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("380x200")
        self.resizable(False, False)

        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.ent_radio = tk.Entry(self)
        self.ent_radio.place(x=110, y=20, width=135)

        tk.Button(self, text="Calcular", command=self._calcular).place(x=110, y=50, width=135)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=100, width=240)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=130, width=240)

        agregar_imagen_figura(self, "esfera")

    def _calcular(self):
        try:
            esf = Esfera(float(self.ent_radio.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {esf.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {esf.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo vacío o formato numérico no válido")


class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("380x240")
        self.resizable(False, False)

        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.ent_base = tk.Entry(self)
        self.ent_base.place(x=120, y=20, width=125)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.ent_altura = tk.Entry(self)
        self.ent_altura.place(x=120, y=50, width=125)

        tk.Label(self, text="Apotema (cms):").place(x=20, y=80)
        self.ent_apotema = tk.Entry(self)
        self.ent_apotema.place(x=120, y=80, width=125)

        tk.Button(self, text="Calcular", command=self._calcular).place(x=120, y=110, width=125)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=150, width=240)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=180, width=240)

        agregar_imagen_figura(self, "piramide")

    def _calcular(self):
        try:
            pir = Piramide(float(self.ent_base.get()), float(self.ent_altura.get()), float(self.ent_apotema.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {pir.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {pir.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo vacío o formato numérico no válido")


class VentanaCubo(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cubo")
        self.geometry("380x200")
        self.resizable(False, False)

        tk.Label(self, text="Lado (cms):").place(x=20, y=20)
        self.ent_lado = tk.Entry(self)
        self.ent_lado.place(x=110, y=20, width=135)

        tk.Button(self, text="Calcular", command=self._calcular).place(x=110, y=50, width=135)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=100, width=240)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=130, width=240)

        agregar_imagen_figura(self, "cubo")

    def _calcular(self):
        try:
            cubo = Cubo(float(self.ent_lado.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {cubo.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cubo.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo vacío o formato numérico no válido")


class VentanaPrisma(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Prisma Rectangular")
        self.geometry("380x240")
        self.resizable(False, False)

        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.ent_base = tk.Entry(self)
        self.ent_base.place(x=120, y=20, width=125)

        tk.Label(self, text="Profundidad:").place(x=20, y=50)
        self.ent_prof = tk.Entry(self)
        self.ent_prof.place(x=120, y=50, width=125)

        tk.Label(self, text="Altura (cms):").place(x=20, y=80)
        self.ent_altura = tk.Entry(self)
        self.ent_altura.place(x=120, y=80, width=125)

        tk.Button(self, text="Calcular", command=self._calcular).place(x=120, y=110, width=125)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=150, width=240)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=180, width=240)

        agregar_imagen_figura(self, "prisma")

    def _calcular(self):
        try:
            prisma = Prisma(float(self.ent_base.get()), float(self.ent_prof.get()), float(self.ent_altura.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {prisma.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {prisma.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo vacío o formato numérico no válido ")



class VentanaPrincipalFiguras(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("250x280")
        self.resizable(False, False)

        tk.Button(self, text="Cilindro", command=lambda: VentanaCilindro(self)).place(x=30, y=20, width=190, height=35)
        tk.Button(self, text="Esfera", command=lambda: VentanaEsfera(self)).place(x=30, y=70, width=190, height=35)
        tk.Button(self, text="Pirámide", command=lambda: VentanaPiramide(self)).place(x=30, y=120, width=190, height=35)
        tk.Button(self, text="Cubo", command=lambda: VentanaCubo(self)).place(x=30, y=170, width=190, height=35)
        tk.Button(self, text="Prisma", command=lambda: VentanaPrisma(self)).place(x=30, y=220, width=190, height=35)

if __name__ == "__main__":
    VentanaPrincipalFiguras().mainloop()