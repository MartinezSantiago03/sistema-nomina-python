import tkinter as tk

def mostrar_reporte(emp,total):

    ventana = tk.Toplevel()
    ventana.title("Reporte de Nómina")
    ventana.geometry("350x300")

    titulo = tk.Label(
        ventana,
        text="Reporte de Pago",
        font=("Arial",14,"bold")
    )

    titulo.pack(pady=10)

    datos = [
        f"Identificación: {emp.identificacion}",
        f"Nombre: {emp.nombre}",
        f"Género: {emp.genero}",
        f"Cargo: {emp.cargo}",
        f"Días trabajados: {emp.dias}",
        f"Valor día: {emp.valor_dia}",
        f"Fecha: {emp.fecha}",
        f"Total a pagar: {total}"
    ]

    for d in datos:
        tk.Label(ventana,text=d).pack()