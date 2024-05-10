#Definnir
factorial=1

numero=int(input("Ingrese un numero para su factorial: "))
rango=range(1,numero+1)
print(f"\nFactorial de {numero}\n")
for i in rango:
    factorial=factorial*i
    print(f"{i} - {factorial} = {factorial*i}")
print(f"El fatorial de {numero} es igul a {factorial}");