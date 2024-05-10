diurno=0.10;
vespertino=0.15;
total=0;
valor=0;

respuesta=input("Pertenece a la joranada diuerno o vespertina: ");

if(respuesta.lower=="diurno"):
    print("Ustede tiene un descuento del 10%");
    total=valor*diurno
elif(respuesta=="vespertino"):
    print("Usted tiene un descuento del 15%");
    total=valor*vespertino
else:
    print("Se nota que tus papás son primos");
