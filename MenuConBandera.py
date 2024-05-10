#declarar variables
flag=True;

#menu de opciones

while flag==True:
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
            print("ingresaste a la opcion 1.");
        elif opcion==2:
            print("ingresaste a la opcion 2.");
        elif opcion==3:
            print("ingresaste a la opcion 3."); 
        elif opcion==4:
            print("ingresaste a la opcion 4."); 
            print("Saliendo del programa");
            flag=False;
        else:
            print("ingrese una opcion valida. vuelva a intentarlo");
