import tkinter as tk
from tkinter import ttk


def mostrar_reporte(emp, total):

    ventana = tk.Toplevel()
    ventana.title("Reporte de Nómina")
    ventana.geometry("350x320")

    frame = ttk.Frame(ventana, padding=20)
    frame.pack(expand=True)

    ttk.Label(
        frame,
        text="Reporte de Pago",
        font=("Segoe UI", 13, "bold")
    ).pack(pady=10)

    datos = [
        f"Identificación: {emp.identificacion}",
        f"Nombre: {emp.nombre}",
        f"Género: {emp.genero}",
        f"Cargo: {emp.cargo}",
        f"Días trabajados: {emp.dias}",
        f"Valor día: ${emp.valor_dia}",
        f"Fecha: {emp.fecha}",
        f"TOTAL A PAGAR: ${total}"
    ]

    for dato in datos:
        ttk.Label(frame, text=dato).pack(anchor="w", pady=2)