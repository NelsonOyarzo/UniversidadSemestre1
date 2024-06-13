lista=[];
for i in range(10):
    try:
        num=int(input("Ingrese un número: "));
    except:
        print("Ingrese un valor valido;");
    else:
        lista.append(num);
        resultado=resultado+num


print(f"Los numeros que ingreso son: {lista}");
print(f"El resultado de la suma de esos numeros es: {resultado}");
print(f"El promedio de lso numeros es: {resultado/10}");
