datos="""¿Qué tengo que hacer
Pa' que tú sea' mi mujer?
Baby, dime qué tengo que hacer
He said: Mi nena

Tú ere' una diabla
Y tú ere' mala
Baby, no te vaya'
Mátame-eh

Tú ere' una diabla
Y tú ere' mala
Baby, no te vaya'
Devórame-eh

Oh-oh-oh-oh
Sé que me extraña'
Oh-oh-oh-oh
Tú en mi cama

Baby, tú ere' mala
Tú en mi cama
Baby, no te vaya'
Devórame-eh, uah

¿Qué tengo que hacer
Pa' que tú sea' mi mujer?
Baby, ¿dime qué tengo que hacer
Pa' que tú seas mi mujer?
Uah (Uah)

¿Qué tengo que hacer (bebé)
Pa' que tú sea' mi mujer? (bebé)
Baby, ¿dime qué tengo que hacer (que hacer)
Pa' que tú sea' mi mujer? (mujer)

Yo voy con lo' diablo' pa' allá
Ven con tus amigas pa' acá
Rebota esas nalga' pa' acá
Y nos vamo' y nos comemo' allá (allá)

Yo voy con los diablo pa' allá, pa' allá (bebé)
Baby, ven con tus amigas pa' acá, pa' acá (bebé)
Rebota esas nalga' pa' atrá', pa' atrá' (pa' allá)
Y nos vamo' y nos comemo' allá (allá)

Baby, tú ere' mala
Tú en mi cama
Baby, no te vayas
Devórame-eh, uah

Tú ere' una diabla
Y tú ere' mala
Baby, no te vaya'
Mátame-eh

Oh-oh-oh-oh (baby)
Bebiendo baila
Oh-oh-oh-oh
Diabla en mi cama

Dos mil, Louis Vuitton y los tacone' (tacone')
Ella se emborracha y en cuatro se pone (se pone)
Y siempre me pide que no la traicione
Y siempre lo hacemo', pero sin condone', eh-eh (uah)
Y se me trepa encima (encima)
Y 'tá to' moja'o el clima (el clima)
Y con la perla yo voy pa' encima (uah)
Y me dice: Qué rico tú me lastimas, uah
Sudando y bailándome (eh-eh)
Caliente y tocándome (eh-eh)
Y ella no para de beber (beber)
Y adentro 'e ti yo vo' a enloquecer

Tú ere' una diabla
Y tú ere' mala
Baby, no te vaya'
Mátame-eh

Baby, tu ere' mala
Tú en mi cama
Baby, no te vaya'
Devórame-eh (oh-oh-oh-oh-oh-oh)

Real hasta la muerte, baby
Real hasta la muerte, baby
Uah
Mera, dime 6ix9ine
Lo' Intocable', lo' Illuminati
Anuel
Uah, uah
Bebecita
Bebe-Bebecita"""

#Crear un contexto para abrir un nuevo archivo
"""
with open('16.0.TXT/Archivo nuevo.txt','w',encoding='utf-8') as archivo:
    archivo.write(datos)
print("Se creo el archivo correctamente")


#Crear contexto para abrir y leer el comtenido

with open('16.0.TXT/Archivo nuevo.txt','r',encoding='utf-8') as archivo:
    print(archivo.read())#Funcion sin parametros y con retorno


#Manejo de archivos csv

import csv
encabezado=['Nombre','Edad','Comuna']
matrizDatos=[
    ['Luis','24','Puerto Montt'],
    ['Claudio','15','Llanquihue'],
    ['Nicolás','21','Puerto Varas']
    ]

#Se crea el contexto para abrir el archivo csv
with open('16.0.TXT/Archivo_nuevo.csv','w',newline='',encoding='utf-8') as archivo:
    archivo_csv=csv.writer(archivo)
    archivo_csv.writerow(encabezado)
    archivo_csv.writerows(matrizDatos)
print("El archivo se creo de forma correcta")

import csv
#Se crea el contexto para abrir el archivo csv
with open('16.0.TXT/Archivo_nuevo.csv','r',newline='',encoding='utf-8') as archivo:
    archivo_csv=csv.reader(archivo)
    for x in archivo_csv:
        print(x)
"""

import csv
#Se crea el contexto para leer el archivo csv
with open('16.0.TXT/Archivo_nuevo.csv','r',newline='',encoding='utf-8') as archivo:
    archivo_csv=csv.DictReader(archivo)
    for x in archivo_csv:
        nombre=x['Nombre']
        edad=int(x['Edad'])
        comuna=x['Comuna']
        if edad>=18:
            esMayor="Es mayor de edad"
        else:
            esMayor="Es menor de edad"
        print(f"{nombre} tiene {edad} anos y {esMayor}.")