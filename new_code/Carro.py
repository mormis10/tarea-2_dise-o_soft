from Vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, color, peso, ruedas=4, es_electrico=False, capacidad_pasajeros=4):
        super().__init__(color, peso, ruedas, es_electrico, capacidad_pasajeros)
        self.tipo = "Carro"
        self.costo_base = 15000

    def calcular_costo(self):
        total = 0
        if self.es_electrico:
            total += 5000
        total = self.costo_base + (self.peso * 100)
        return total
    
    def necesita_inspeccion(self):
        if self.peso > 2000:
            return True
        return False
    
    def imprimir_datos(self):
        print(f"Tipo: {self.tipo}")
        super().imprimir_datos()