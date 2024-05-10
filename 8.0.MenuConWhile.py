#declarar variables
num1=0
num2=0
#menu de opciones

while True:
    print("-----Menu de opciones-----");
    print("1.- sumar dos numeros.");
    print("2.- saber si el numero es par.");
    print("3.- dibujar un cuadrado.");
    print("4.- salir del programa.");
    try:
       opcion=int(input("** ingrese una opcion--> "));
    except ValueError:
        print("vuelva a intentarlo debe ser un NUMERO de 1 al 4");
    else:
        if opcion==1:
            while True:
                print("ingresaste a la opcion 1.\n");
                try:
                    num1=int(input("Ingrese el primer numero: "));
                    num2=int(input("Ingrese el primer numero: "));
                except ValueError:
                    print("Ingrese un numero tonto weon, intentelo de nuevo");
                else:
                    resultado=num1+num2
                    print(f"El resultado es {resultado}\n");
                    break;
        elif opcion==2:
            while True:
                print("ingresaste a la opcion 2.");
                try:
                    num1=int(input("Ingrese un numero: "));
                except ValueError:
                    print("Ingrese un numero tonto weon, intentelo de nuevo");
                else:
                    resto=(num1%2);
                    if (resto==0):
                        print("El numero que ingreso es par");
                    else:
                        print("El numero que ingreso es impar");
                    break;
        elif opcion==3:
            while True:
                print("ingresaste a la opcion 3.");
                try:
                    lado=int(input("Ingrese el tamaño del lado del cuadrado: "));
                except ValueError:
                    print("Ingrese un numero tonto weon, intentelo de nuevo.");
                else:
                    for j in range(lado):
                        for i in range(lado):
                            print(" * ",end="");
                        print("")
                    break;
        elif opcion==4:
            print("ingresaste a la opcion 4."); 
            print("Saliendo del programa");
            break;
        else:
            print("ingrese una opcion valida. vuelva a intentarlo");