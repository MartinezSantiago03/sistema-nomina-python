import tkinter as tk
from tkinter import ttk
from utils.constantes import VALORES_CARGO
from model.gestion_empleados import GestionEmpleados
from gui.reporte import mostrar_reporte

def abrir_registro():

    ventana = tk.Tk()
    ventana.title("Registro de Empleado")
    ventana.geometry("450x400")

    frame = tk.Frame(ventana,padx=20,pady=20)
    frame.pack()

    tk.Label(frame,text="Identificación").grid(row=0,column=0)
    entry_id = tk.Entry(frame)
    entry_id.grid(row=0,column=1)

    tk.Label(frame,text="Nombre").grid(row=1,column=0)
    entry_nombre = tk.Entry(frame)
    entry_nombre.grid(row=1,column=1)

    tk.Label(frame,text="Genero").grid(row=2,column=0)

    genero = tk.StringVar()

    ttk.Radiobutton(frame,text="Masculino",variable=genero,value="Masculino").grid(row=2,column=1)
    ttk.Radiobutton(frame,text="Femenino",variable=genero,value="Femenino").grid(row=2,column=2)

    tk.Label(frame,text="Cargo").grid(row=3,column=0)

    cargo = ttk.Combobox(frame,values=list(VALORES_CARGO.keys()))
    cargo.grid(row=3,column=1)

    tk.Label(frame,text="Valor Día").grid(row=4,column=0)

    valor_dia = tk.Entry(frame,state="readonly")
    valor_dia.grid(row=4,column=1)

    tk.Label(frame,text="Días Trabajados").grid(row=5,column=0)

    dias = tk.Entry(frame)
    dias.grid(row=5,column=1)

    def actualizar_valor(event):
        valor = VALORES_CARGO.get(cargo.get(),0)

        valor_dia.config(state="normal")
        valor_dia.delete(0,tk.END)
        valor_dia.insert(0,str(valor))
        valor_dia.config(state="readonly")

    cargo.bind("<<ComboboxSelected>>",actualizar_valor)

    def calcular():

        empleado = GestionEmpleados(
            entry_id.get(),
            entry_nombre.get(),
            genero.get(),
            cargo.get(),
            int(dias.get()),
            float(valor_dia.get())
        )

        total = empleado.calcular_nomina()

        mostrar_reporte(empleado,total)

    tk.Button(
        frame,
        text="Calcular Nomina",
        bg="#2196F3",
        fg="white",
        command=calcular
    ).grid(row=6,column=0,pady=20)

    tk.Button(
        frame,
        text="Salir",
        bg="#f44336",
        fg="white",
        command=ventana.quit
    ).grid(row=6,column=1)

    ventana.mainloop()