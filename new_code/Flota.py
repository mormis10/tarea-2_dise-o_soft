from Camión import Camion
from Carro import Carro
from Motocicleta import Motocicleta


class Flota:
    def __init__(self):
        self.vehiculos = []
    
    def agregar_vehiculo(self):
        tipo = input("Tipo (auto/moto/camion): ").lower()
        color = input("Color: ")
        peso = float(input("Peso (kg): "))
        electrico = input("Es eléctrico? (s/n): ").lower() == 's'

        if tipo == 'moto':
            vehiculo = Motocicleta(
                color=color,
                peso=peso,
                es_electrico=electrico
            )
        elif tipo == 'auto':
            vehiculo = Carro(
                color=color,
                peso=peso,
                es_electrico=electrico
            )
        elif tipo == 'camion':
            vehiculo = Camion(
                color=color,
                peso=peso,
                es_electrico=electrico
            )
        else:
            print("Tipo de vehículo no válido!")
            return

        self.vehiculos.append(vehiculo)
        print("Vehículo agregado!")
    
    def get_vehiculos(self):
        return self.vehiculos

    def generar_reporte(self):
        from Generador_reportes import Generador_Reportes
        reporte = Generador_Reportes(self.get_vehiculos())
        reporte.generador_reportes()
