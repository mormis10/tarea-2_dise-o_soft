from Motocicleta import Motocicleta
from Camión import Camion
from Carro import Carro
prueba = Motocicleta("azul",20)

valor = prueba.calcular_costo()

print(valor)
print("\n")
prueba1 = Camion("Verde",5000)

valor2 = prueba1.calcular_costo()
print(valor2)
print("\n")

prueba2 = Carro("Lila",300)

valor3 = prueba2.calcular_costo()
print(valor3)

