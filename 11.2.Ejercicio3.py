lista=[]

for i in range(10):
    num = int(input("Ingrese un número entero: "))
    lista.append(num)

suma = sum(lista)

promedio = suma / len(lista)

# Mostrar la suma y el promedio
print(f"La suma de los números es: {suma}")
print(f"El promedio de los números es: {promedio:.2f}")
