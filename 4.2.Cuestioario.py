#Declarar variables
cont=0

print("Vienvennido a el concursillo\n")
print("En que año fue la caida de Reach\n")
print("a).-2550")
print("b).-2552")
print("c).-2556")
print("d).-2548")

opcion=input("Elija una opcion: ")
if (opcion=="a"):
    print("Incorrecto");
elif (opcion=="b"):
    print("Correcto")
    cont=cont+1
elif (opcion=="c"):
    print("Incorrecto")
else:
    print("Incorrecto")

print("Como se llama el protagonista de Persona 5\n")
print("a).-Joker")
print("b).-Temperance")
print("c).-Fortune")
print("d).-Death")

opcion=input("Elija una opcion: ")
if (opcion=="a"):
    print("Correcto")
    cont=cont+1
elif (opcion=="b"):
    print("Incorrecto")
elif (opcion=="c"):
    print("Incorrecto")
else:
    print("Incorrecto")

print("Quien desarrollo kingdom hearts\n")
print("a).-Atlus")
print("b).-Nintendo")
print("c).-Konami")
print("d).-Square Enix")

opcion=input("Elija una opcion: ")
if (opcion=="a"):
    print("Incorrecto")
elif (opcion=="b"):
    print("Incorrecto")
elif (opcion=="c"):
    print("Incorrecto")
else:
    print("Correcto")
    cont=cont+1

print(f"Su puntaje es de {cont}")