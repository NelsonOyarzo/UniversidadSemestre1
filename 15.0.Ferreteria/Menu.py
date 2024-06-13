import Funciones as funcion

while True:
    print("Ferreteria")
    print("Agregar producto")
    print("Mostrar producto")
    print("Buscar producto")
    print("Eliminar Producto")
    print("Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        funcion.agregarProducto()
    elif opcion==2:
        funcion.mostrarProducto()
    elif opcion==3:
        funcion.mostrarProduct0()
        producto=input("Ingrese el producto que desea buscar: ")
        print(funcion.buscarProducto)
    elif opcion==4:
        funcion.eliminarProducto()
    elif opcion==5:
        print("Saliendo del programa")
        break
    else:
        print("Ingrese una opcion valida")