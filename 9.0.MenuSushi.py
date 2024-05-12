#Declarar variables
PikachuRoll=4500
OtakuRoll=5000
PulpoVenenosoRoll=5200
AnguilaEléctricaRoll=4800
ConPikachuRoll=0
ConOtakuRoll=0
ConPulpoVenenosoRoll=0
ConAnguilaEléctricaRoll=0
TotalPago=0
#Menu

while True:
    print("Bienvenido a delivery sushi");
    print("\nMenu1");
    print("1.-Pikachu Roll $4500");
    print("2.-Otaku Roll $5000");
    print("3.-Pulpo Venenoso Roll $5200");
    print("4.-Anguila Eléctrica Roll $4800");
    print("5.-Terminar pedido")
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Ingrese una opción válida, vuelva a intentarlo")
    else:
        if (opcion==1):
            ConPikachuRoll=ConPikachuRoll+1
            TotalPago=TotalPago+PikachuRoll
        elif (opcion==2):
            ConOtakuRoll=ConOtakuRoll+1
            TotalPago=TotalPago+OtakuRoll
        elif (opcion==3):
            ConPulpoVenenosoRoll=ConPulpoVenenosoRoll+1
            TotalPago=TotalPago+PulpoVenenosoRoll
        elif (opcion==4):
            ConAnguilaEléctricaRoll=ConAnguilaEléctricaRoll+1
            TotalPago=TotalPago+AnguilaEléctricaRoll
        elif (opcion==5):
            print(f"Total Productos {ConPikachuRoll+ConOtakuRoll+ConPulpoVenenosoRoll+ConAnguilaEléctricaRoll}\n");
            print(f"1.-Pikachu Roll------------{ConPikachuRoll}");
            print(f"2.-Otaku Roll--------------{ConOtakuRoll}");
            print(f"3.-Pulpo Venenoso Roll-----{ConPulpoVenenosoRoll}");
            print(f"4.-Anguila Eléctrica Roll--{ConAnguilaEléctricaRoll}\n");
            print(f"Subtotal por pagar: {TotalPago}")
            while True:
                opcdescuento = input("¿Posee un código de descuento? (s/n): ")
                if opcdescuento == "s":
                    codigo = input("Ingrese el código de descuento: ")
                    if codigo == "otaku":
                        print(f"Total Productos {ConPikachuRoll+ConOtakuRoll+ConPulpoVenenosoRoll+ConAnguilaEléctricaRoll}\n")
                        print(f"1.-Pikachu Roll------------{ConPikachuRoll}")
                        print(f"2.-Otaku Roll--------------{ConOtakuRoll}")
                        print(f"3.-Pulpo Venenoso Roll-----{ConPulpoVenenosoRoll}")
                        print(f"4.-Anguila Eléctrica Roll--{ConAnguilaEléctricaRoll}\n")
                        print(f"Subtotal por pagar: {TotalPago}")
                        Descuento = TotalPago * 0.10
                        print(f"Descuento por código: {Descuento}")
                        print(f"Total: {TotalPago-Descuento}")
                    else:
                        print("Código incorrecto, vuelva a intentarlo")
                elif opcdescuento == "n":
                    print(f"Total Productos {ConPikachuRoll+ConOtakuRoll+ConPulpoVenenosoRoll+ConAnguilaEléctricaRoll}\n")
                    print(f"1.-Pikachu Roll------------{ConPikachuRoll}")
                    print(f"2.-Otaku Roll--------------{ConOtakuRoll}")
                    print(f"3.-Pulpo Venenoso Roll-----{ConPulpoVenenosoRoll}")
                    print(f"4.-Anguila Eléctrica Roll--{ConAnguilaEléctricaRoll}\n")
                    print(f"Subtotal por pagar: {TotalPago}")
                    print("Descuento por código: 0")
                    print(f"Total: {TotalPago}")
                    break
                else:
                    print("Opción no válida")

                    
                    