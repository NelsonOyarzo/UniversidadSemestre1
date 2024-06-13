#SUMAR NUMEROS
def sumarDosNumeros():
    num1=int(input("Ingrese un numero:"))
    num2=int(input("Ingrese un numero:"))
    suma=(num1+num2)
    print(f"El resultado es {suma}")

sumarDosNumeros()
#SUMAR CON PARAMETROS
def sumarDosNumerosConParametros(num1,num2):
    suma=(num1+num2)
    print(f"El resultado es {suma}")

sumarDosNumerosConParametros(6,5)
#SUMAR CON RETORNO

def sumarDosNumerosConRetorno():
    num1=int(input("Ingrese un numero:"))
    num2=int(input("Ingrese un numero:"))
    suma=(num1+num2)
    return suma

print(f"El resultado es {sumarDosNumerosConRetorno()+10}")
#SUMAR CON PARAMETROS Y CON RETORNO
def sumarDosNumerosConParametrosRetorno(num1,num2):
    suma=(num1+num2)
    return suma

print(f"El resultado es {sumarDosNumerosConParametrosRetorno(1,0)+10}")