import random
import time

lista_numero=[]

print("\nBienvenido la loteria")
print("Ingrese sus 5 numeros de la suerte: ")

for i in range(5):
    num=int(input("Ingrese sus numeros: "))
    lista_numero.append(num)

print(f"Sus numeros de la suerte son: {lista_numero}")
lista_aleatoria=[]

for i in range(5):
    while True:
        num_aleatorio=random.randint(1,11)
        time.sleep(2)
        print(f"El numero generado es: {num_aleatorio}")
        if num_aleatorio not in  lista_aleatoria:
            lista_aleatoria.append(num_aleatorio)
            break

print(f"La lista generada es: {lista_aleatoria}")

contador=0

for x in lista_numero:
    if x in lista_aleatoria:
        contador=contador+1

if contador==5:
    print("FELICIDADES GANASTE TU PREMIO")
else:
    print("SUERTE A LA PROXIMA")