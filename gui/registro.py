import tkinter as tk
from tkinter import ttk, messagebox
from utils.constantes import VALORES_CARGO
from model.gestion_empleados import GestionEmpleados
from gui.reporte import mostrar_reporte


def abrir_registro():

    ventana = tk.Tk()
    ventana.title("Registro de Empleado")
    ventana.geometry("500x420")

    frame = ttk.Frame(ventana, padding=20)
    frame.pack(expand=True)

    ttk.Label(frame, text="Registro de Empleado",
              font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    # Campos

    ttk.Label(frame, text="Identificación").grid(row=1, column=0, sticky="w")
    entry_id = ttk.Entry(frame)
    entry_id.grid(row=1, column=1)

    ttk.Label(frame, text="Nombre Completo").grid(row=2, column=0, sticky="w")
    entry_nombre = ttk.Entry(frame)
    entry_nombre.grid(row=2, column=1)

    ttk.Label(frame, text="Genero").grid(row=3, column=0, sticky="w")

    genero = tk.StringVar()

    ttk.Radiobutton(frame, text="Masculino",
                    variable=genero, value="Masculino").grid(row=3, column=1)

    ttk.Radiobutton(frame, text="Femenino",
                    variable=genero, value="Femenino").grid(row=3, column=2)

    ttk.Label(frame, text="Cargo").grid(row=4, column=0, sticky="w")

    cargo = ttk.Combobox(frame, values=list(VALORES_CARGO.keys()))
    cargo.grid(row=4, column=1)

    ttk.Label(frame, text="Valor Día").grid(row=5, column=0, sticky="w")

    valor_dia = ttk.Entry(frame, state="readonly")
    valor_dia.grid(row=5, column=1)

    ttk.Label(frame, text="Días Trabajados").grid(row=6, column=0, sticky="w")

    dias = ttk.Entry(frame)
    dias.grid(row=6, column=1)

    # Mostrar valor según cargo

    def actualizar_valor(event):
        valor = VALORES_CARGO.get(cargo.get(), 0)

        valor_dia.config(state="normal")
        valor_dia.delete(0, tk.END)
        valor_dia.insert(0, str(valor))
        valor_dia.config(state="readonly")

    cargo.bind("<<ComboboxSelected>>", actualizar_valor)

    # Validaciones

    def validar_campos():

        if entry_id.get() == "":
            messagebox.showwarning("Error", "Ingrese la identificación")
            return False

        if entry_nombre.get() == "":
            messagebox.showwarning("Error", "Ingrese el nombre")
            return False

        if genero.get() == "":
            messagebox.showwarning("Error", "Seleccione el género")
            return False

        if cargo.get() == "":
            messagebox.showwarning("Error", "Seleccione un cargo")
            return False

        if dias.get() == "":
            messagebox.showwarning("Error", "Ingrese los días trabajados")
            return False

        if not dias.get().isdigit():
            messagebox.showwarning("Error", "Los días deben ser números")
            return False

        return True

    # Calcular nómina

    def calcular():

        if not validar_campos():
            return

        empleado = GestionEmpleados(
            entry_id.get(),
            entry_nombre.get(),
            genero.get(),
            cargo.get(),
            int(dias.get()),
            float(valor_dia.get())
        )

        total = empleado.calcular_nomina()

        mostrar_reporte(empleado, total)

    # Botones

    ttk.Button(
        frame,
        text="Calcular Nómina",
        command=calcular
    ).grid(row=7, column=0, pady=20)

    def salir():
        confirmacion = messagebox.askyesno(
            "Salir",
            "¿Está seguro que desea salir?"
        )
        if confirmacion:
            ventana.destroy()

    ttk.Button(
        frame,
        text="Salir",
        command=salir
    ).grid(row=7, column=1)

    ventana.mainloop()