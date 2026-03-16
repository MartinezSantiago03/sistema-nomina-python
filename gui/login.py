import tkinter as tk
from tkinter import ttk, messagebox
from utils.constantes import PASSWORD
from gui.registro import abrir_registro


def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


def iniciar_login():

    ventana = tk.Tk()
    ventana.title("Sistema de Nómina")
    centrar_ventana(ventana, 400, 250)

    frame = ttk.Frame(ventana, padding=20)
    frame.pack(expand=True)

    titulo = ttk.Label(
        frame,
        text="Sistema de Gestión de Nómina",
        font=("Segoe UI", 14, "bold")
    )
    titulo.pack(pady=10)

    autor = ttk.Label(
        frame,
        text="Autor: Santiago Martínez Herrera"
    )
    autor.pack()

    ttk.Label(frame, text="Ingrese contraseña").pack(pady=10)

    password = ttk.Entry(frame, show="*", width=25)
    password.pack()

    def validar():

        if password.get() == PASSWORD:
            ventana.destroy()
            abrir_registro()
        else:
            messagebox.showerror(
                "Error de acceso",
                "La contraseña ingresada es incorrecta"
            )

    boton = ttk.Button(
        frame,
        text="Ingresar",
        command=validar
    )

    boton.pack(pady=20)

    ventana.mainloop()