#Declarar variable y constantes
precioChurrasco=1500;
precioCompleto=1500;
precioCvegetariano=1500;
precioBarrosluco=1500;
totalCompra=0;
CantidadChurrascos=0;
CantidadCompleto=0;
CantidadCvegetariano=0;
CantidadBarrosluco=0;
descuento=0.1;
respuesta="";
codigoh="hunterxhunter";
#Mostrar precios
print("Bienvenido a la sandwicheria tu mamá la mas rica\n")
print("Lista de precios\n")
print("1.-Churrascos----$1.500\n2.-Completos----$1.000\n1.-Vegetariano----$2.000\n1.-Barros Luco----$3.000");

#Solicitar la cantidad
CantidadChurrascos=int(input("Cuantos Churrascos quiere"));
CantidadCompleto=int(input("Cuantos Completos quiere"));
CantidadCvegetariano=int(input("Cuantos Vegetarianos quiere"));
CantidadBarrosluco=int(input("Cuantos Barros Luco quiere"));

#Calcular total
totalCompra=totalCompra+(CantidadChurrascos*precioChurrasco);
totalCompra=totalCompra+(CantidadCompleto*precioCompleto);
totalCompra=totalCompra+(CantidadCvegetariano*precioCvegetariano);
totalCompra=totalCompra+(CantidadBarrosluco*precioBarrosluco);

#Motrar total de compra
print(f"El total de la compra es {totalCompra}\n")

#Descuento y validacion
respuesta=input("Tiene un cupon de descuento?s/n")

if(respuesta=="s"):
    codigo=input("Ingrese el codigo de descuento: ");
    if(codigo==codigoh):
            totalCompra=totalCompra-(totalCompra*descuento);
            print("Usted tiene un descueunto del 10%");
            print(f"El total de su compra es ${totalCompra}");
    else:
        print("codigo incorrecto")
elif(respuesta=="n"):
    print("Usted no tiene descuento")
    print(f"El total de la compra es{totalCompra}\n")
else:
    print("Que aweona se equivoco, vuelva a intentarlo")

print("\nGracias por su compra disfrute a su mamá\n")