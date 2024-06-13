import random

numerosJugador = set()
print("Ingrese 7 números únicos del 1 al 49:")
while len(numerosJugador) < 7:
    try:
        numero = int(input(f"Ingrese el número {len(numerosJugador) + 1}: "))
        if numero < 1 or numero > 49:
            raise ValueError("El número debe estar entre 1 y 49. Intente de nuevo.")
        elif numero in numerosJugador:
            print("Ya ingresaste ese número. Intente de nuevo.")
        else:
            numerosJugador.add(numero)
    except ValueError as e:
        print(e)

rondas_ganadoras = []
for _ in range(3):
    numeros_ganadores = tuple(random.sample(range(1, 50), 7))
    rondas_ganadoras.append(numeros_ganadores)

aciertos_por_ronda = {}
for i, ronda in enumerate(rondas_ganadoras):
    aciertos = len(numerosJugador.intersection(set(ronda)))
    aciertos_por_ronda[f"Ronda {i+1}"] = aciertos

ganador = any(aciertos > 0 for aciertos in aciertos_por_ronda.values())

print(f"Números del jugador: {numerosJugador}")
for i, ronda in enumerate(rondas_ganadoras):
    print(f"Números ganadores de la ronda {i+1}: {ronda}")
    print(f"Aciertos en la ronda {i+1}: {aciertos_por_ronda[f'Ronda {i+1}']}")

if ganador:
    print("¡Felicidades! Has ganado.")
else:
    print("Lo siento, no has ganado esta vez.")

#Diego Benitiz
#Matias Caileo
#Nelson Oyarzo