from Flota import Flota

#Esta prueba es para marco

prueba = Flota()
print("Bienvenido, a la prueba de nacho, es un ciclo donde se ingresaran autos 5, para la prueba, luego se genera un reporte de los mismos\n")
for i in range(6):
    prueba.agregar_vehiculo()


prueba.generar_reporte()

