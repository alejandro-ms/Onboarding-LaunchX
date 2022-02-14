# Para este ejercicio, escribirás una lógica condicional
# que imprima una advertencia si un asteroide se acerca a la Tierra demasiado rápido.
# La velocidad del asteroide varía dependiendo de lo cerca que esté del sol,
# y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.

asteroid = 49
if(asteroid > 25):
    print("El asteroide se acerca a la tierra demasiado rapido")
else:
    print("No hay peligro alguno")

# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s,
#  a veces produce un rayo de luz que se puede ver desde la Tierra. Escribe la
#  lógica condicional que
# usa declaraciones if, else, y elif para alertar a las personas de todo el mundo que
# deben buscar un asteroide en el cielo. ¡Hay
# uno que se dirige a la tierra ahora a una velocidad de 19 km/s!

asteroid = 19
if(asteroid >= 20):
    print("El asteroide es visible")
else:
    print("El asteroide no es visible")

asteroidSize = 25
asteroidSpeed = 20
if(asteroidSize < 25):
    print("El asteroide se quema al entrar a la atmósfera")
elif(asteroidSize > 25 and asteroidSize <= 1000):
    print("Cuidado el asteroide golpeara a la tierra")
if(asteroidSpeed > 25):
    print("Cuidado con el asteroide")
if(asteroidSpeed >= 20):
    print("Rayo de luz visible")
else:
    print("Todo correcto siga con su dia")


# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

velocidad_asteroide = 25
tamano_asteroide = 40
if velocidad_asteroide > 25 and tamano_asteroide > 25:
    print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_asteroide >= 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif tamano_asteroide < 25:
    print('Nada que ver aquí :)')
else:
    print('Nada que ver aquí :)')
