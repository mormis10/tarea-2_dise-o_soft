from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, color, peso, ruedas=2, es_electrico=False, capacidad_pasajeros=2):
        super().__init__(color, peso, ruedas, es_electrico, capacidad_pasajeros)
        self.tipo = "Motocicleta"
        self.costo_base = 8000

    def calcular_costo(self):
        total = 0
        if self.es_electrico:
            total += 3000 
        total = self.costo_base + (self.peso * 50)
        return total
    
    def necesita_inspeccion(self):
        if self.peso > 300:
            return True
        return False
    
    def imprimir_datos(self):
        print(f"Tipo: {self.tipo}")
        super().imprimir_datos()