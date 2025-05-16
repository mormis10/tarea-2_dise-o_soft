## Tarea#2

## Diego Cerdas Delgado C21988

## Enunciado
# Para la entrega de este trabajo se solicitó Refactorizar un códifo que simulaba una flotilla de distintos tipos de vehículos, esto con la intención de aplicar el uso de buenas prácticas de programación y principios de diseño.

## Análisis

# En el codigo facilitado existía una sola interfaz general llamada vehículo, en busca de poner en práctica el principio SOLID de Interface Segregation Principle, donde principalmente se busca la creación de múltiples interfáces específicas que implementen solo lo que necesitan. Por lo tanto la clase vehículo se transformó en una clase abstracta que dio origen a las clases Camión. 

![Clase Carro](images/Carro.png)
![Clase Camión](images/Camión.png)
![Clase Motocicleta](images/Motocicleta.png)