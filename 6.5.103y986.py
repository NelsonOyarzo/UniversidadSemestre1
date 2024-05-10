num = 0
resto = 0
division = 0
rango = range(2)
numnuevo = 0
division2 = 0
resto2 = 0

num = int(input("Ingrese un numero entre 103 y 987: "))
if num > 103 and num < 987:
    division = num // 10
    resto = num % 10
    division2 = division % 10
    numnuevo = (resto * 10) + division
    print(f"{numnuevo}\n{division}\n{resto}\n{num}")
else:
    print("Numero incorrecto")
