import tkinter as tk
from tkinter import messagebox
from utils.constantes import PASSWORD
from gui.registro import abrir_registro

def iniciar_login():

    ventana = tk.Tk()
    ventana.title("Sistema de Nómina")
    ventana.geometry("350x250")
    ventana.configure(bg="#f2f2f2")

    titulo = tk.Label(
        ventana,
        text="Sistema Gestión de Nómina",
        font=("Arial",14,"bold"),
        bg="#f2f2f2"
    )
    titulo.pack(pady=10)

    autor = tk.Label(
        ventana,
        text="Autor: Santiago Martínez Herrera",
        bg="#f2f2f2"
    )
    autor.pack()

    tk.Label(ventana,text="Ingrese contraseña",bg="#f2f2f2").pack(pady=10)

    password = tk.Entry(ventana,show="*",width=25)
    password.pack()

    def validar():

        if password.get() == PASSWORD:
            ventana.destroy()
            abrir_registro()
        else:
            messagebox.showerror("Error","Contraseña incorrecta")

    boton = tk.Button(
        ventana,
        text="Ingresar",
        bg="#4CAF50",
        fg="white",
        width=15,
        command=validar
    )

    boton.pack(pady=20)

    ventana.mainloop()