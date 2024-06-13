from Calculos import*
import time

n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese otro numero: "))



while True:
    print("\n Hola mundo \n Seleccione una opcion\n")
    print("1.-Sumar")
    print("2.-Restar")
    print("3.-Multiplicar")
    print("4.-Dividir")
    print("5.-Agregar nombres a una lista")
    print("6.-Mostrar la lista")
    print("7.-Eliminar nombre de lista")
    print("8.-Salir")
    try:
        opcion=int(input("Ingrese la operacion que desea realizar: "))
    except:
        print("Error, usted es maricon ingrese un valor valido")
    if opcion==1:
        sumar=sumardosNumeros(n1,n2)
        print(f"El resultado de la suma es :{sumar}")
        time.sleep (2)
    elif opcion==2:
        restar=restardosNumeros(n1,n2)
        print(f"El resultado de la resta es :{restar}")
        time.sleep (2)
    elif opcion==3:
        multiplicar=multiplicardosNumeros(n1,n2)
        print(f"El resultado de la multiplicacion es :{multiplicar}")
        time.sleep (2)
    elif opcion==4:
        dividir=dividirdosNumeros(n1,n2)
        print(f"El resultado de la division es :{dividir}")
        time.sleep (2)
    elif opcion==5:
        agregarNombre()
        time.sleep (1)
    elif opcion==6:
        mostrarNombre()
        time.sleep(1)
    elif opcion==7:
        eliminarNombre()
        time.sleep(1)
    elif opcion==8:
        print("Saliendo de programa")
        break
    else:
        print("Ingrese una opcion valida")