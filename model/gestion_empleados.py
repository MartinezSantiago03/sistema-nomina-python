from datetime import datetime

class GestionEmpleados:

    def __init__(self, identificacion, nombre, genero, cargo, dias, valor_dia):
        self.identificacion = identificacion
        self.nombre = nombre
        self.genero = genero
        self.cargo = cargo
        self.dias = dias
        self.valor_dia = valor_dia
        self.fecha = datetime.now().strftime("%d/%m/%Y")

    def calcular_nomina(self):
        return self.dias * self.valor_dia