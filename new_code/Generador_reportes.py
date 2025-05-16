from typing import List
from Vehiculo import Vehiculo

class Generador_Reportes:
    def __init__(self, lista_vehiculos: List[Vehiculo]):
        self.vdata = lista_vehiculos
    
    def generador_reportes(self):
        total = 0
        electricos = 0
        requieren_inspeccion = 0

        for v in self.vdata:
            v.imprimir_datos()
            total += v.calcular_costo()
            if v.es_electrico:
                electricos += 1
            if v.necesita_inspeccion():
                requieren_inspeccion += 1

        print("\nRESUMEN FLOTA:")
        print(f"Total vehículos: {len(self.vdata)}")
        print(f"Vehículos eléctricos: {electricos}")
        print(f"Requieren inspección: {requieren_inspeccion}")
        print(f"Valor total: ${total}")