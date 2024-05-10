"""
Crea un algoritmo que sea capaz de crear una contraseña ultramente segura de acuerdo a las  siguientes
caracteristicas:
Primeras dos letras de su nombre
Su edad
Primera letra de su nombre y primera letras de su apellido
El mes de su nacimiento en numero
Las ultimas dos letras de la ciudad donde vive
"""
nombre=input("Ingrese su primer nombre: ");
apellido=input("Ingrese su primer apellido:");
edad=int(input("Ingrese su edad: "));
mes=int(input("Ingrese su mes de nacimiento en numero: "));
ciudad=input("Ingrese el nombre de la ciudad donden vive: ");

dosletra=nombre[:2];
piermeraletra=nombre[:1];
primeraapellido=apellido[:1];
utlimaciudad=ciudad[-2:];

#Colocar al principio para tomar los primeros caracteres
#Colocar : al final para tomar los ultimos caracteres

print(f"Su contraseña es: {dosletra}{edad}{piermeraletra}{primeraapellido}{mes}{utlimaciudad}");