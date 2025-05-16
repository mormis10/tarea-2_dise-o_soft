from Vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, color, peso, ruedas=4, es_electrico=False, capacidad_pasajeros=4):
        super().__init__(color, peso, ruedas, es_electrico, capacidad_pasajeros)
        self.tipo = "Camión"
        self.costo_base = 45000

    def calcular_costo(self):
        total = self.costo_base + (self.peso * 200)
        return total
    
    def necesita_inspeccion(self):
        return True
    
    def imprimir_datos(self):
        print(f"Tipo: {self.tipo}")
        super().imprimir_datos()