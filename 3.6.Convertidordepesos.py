"""
===========================================YO===========================================
dolar_australiano=int(input("Ingrese el monto de dolar asutraliano que desa convertir"));
total_australiano=dolar_australiano*615.54
print(total_australiano);
peso_argentino=int(input("Ingrese el monto de peso argentino que desa convertir"));
total_argentino=peso_argentino*1.10
print(total_argentino);
yen=int(input("Ingrese el monto de yen que desa convertir"));
total_yen=yen*6.18
print(total_yen);
"""
#=======================================Profe=======================================
peso_australiano = 615.54
peso_argentino = 1.10
yen = 6.18

print("Convertidor de pesos\n")
peso_chileno = float(input("Ingrese los pesos a convertir: "))

print("1.- A Dólar Australiano")
print("2.- A Peso Argentino")
print("3.- A Yen")

opcion = int(input("Elija una opción: "))

if opcion == 1:
    resultado_australiano = peso_australiano * peso_chileno
    print(f"Resultado: {resultado_australiano}")
elif opcion == 2:
    resultado_argentino = peso_argentino * peso_chileno
    print(f"Resultado: {resultado_argentino}")
elif opcion == 3:
    resultado_yen = yen * peso_chileno
    print(f"Resultado: {resultado_yen}")
else:
    print("Opción no válida")


