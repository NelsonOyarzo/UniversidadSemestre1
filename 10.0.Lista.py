rango=range(4)
texto="Como hace tu mamá";
listaDiscos=["Baby, tú ere mala","Tú en mi cama","Baby, no te vaya","Devórame-eh, uah"];
matriznumerica=[[1,2,3],
                [4,5,6],
                [7,8,9]];

print("\n1) For que recorre un range(5)\n");
for i in rango:
    print(i,end=" - ");

print("\n2) For que recorre un texto\n");
for i in texto:
    print(i,end=" ");

print("\n3) For que recorre una lista \n");
for i in listaDiscos:
    print(i);

print("\n4) For que recorre una matriz \n");
for i in matriznumerica:
    print(i);

for i in matriznumerica:
    for j in i:
        print(j,end=" - ");

for i in rango:
    print("\n",listaDiscos[i]);