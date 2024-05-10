x=range(5)
contnumMa=0
contnumMe=0
contnumI=0
print("Inrgese 5 numeros enteros: ");
for i in x:
    num=int(input("Ingrese un numero "));
    if num<0:
        contnumMa=contnumMa+1
    elif num>0:
        contnumMe=contnumMe+1
    elif num==0:
        contnumI=contnumI+1

print(f"Cantidad de numeros son mayores a 0 = {contnumMa}");
print(f"Cantidad de numeros son menores a 0 = {contnumMe}");
print(f"Cantidad de numeros son iguales a 0 = {contnumI}");



