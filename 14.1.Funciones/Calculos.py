listaNombre=[]

def sumardosNumeros(num1,num2):
    suma=num1+num2;
    return suma

def restardosNumeros(num1,num2):
    resta=num1-num2;
    return resta

def dividirdosNumeros(num1,num2):
    dividir=num1/num2;
    return dividir

def multiplicardosNumeros(num1,num2):
    multiplicar=num1*num2;
    return multiplicar

def agregarNombre():
    nombre=input("Ingrese un nombre: ")
    listaNombre.append(nombre)

def mostrarNombre():
    print(listaNombre)

def eliminarNombre():
    print(f"Lista de nombres {listaNombre}")
    nombre=input("Ingrese el nombre que desea eliminar: ")
    listaNombre.remove(nombre)