listaProductos=["Hacha","Pala","Carretilla","Guantes"]

def agregarProducto():
    producto=input("Ingresar el nuevo producto: ")
    listaProductos.append(producto)
    print("Se ingreso correctamente")

def mostrarProducto():
    print(f"La lista de productos es \n{listaProductos}")

def buscarProducto(producto):
    if producto in listaProductos:
        print("El producto esta en la lista")
        return True
    else:
        print("El producto no esta en la lista")
        return False

def eliminarProducto():
    producto=input("Ingrese el producto que desea aliminar")
    if buscarProducto(producto)==True:
        listaProductos.remove(producto)
        print("El producto se elimino correctamente")
    else:
        print("El producto no se encuentra en la lista")