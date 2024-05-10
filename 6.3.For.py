letra=""
contvocal=0
contconsonante=0
x=range(10)

for i in x:
    letra=input("Ingrese 10 letras: ")
    if (letra=="a") or(letra=="e") or(letra=="i") or(letra=="o") or(letra=="u"):
        contvocal=contvocal+1
    else:
        contconsonante=contconsonante+1

print(f"{contconsonante}  letras son consonante\n")
print(f"{contvocal} letras son vocales")
