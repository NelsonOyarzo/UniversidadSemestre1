# Solicitar tres nombres al usuario
nombres = [];
for i in range(3):
    nombre = input(f"Introduce el nombre {i + 1}: ");
    nombres.append(nombre);

# Encontrar el nombre con mayor cantidad de caracteres
nombre_mas_largo = max(nombres, key=len);

# Mostrar el nombre con mayor cantidad de caracteres
print(f"El nombre con más caracteres es: {nombre_mas_largo}");

print("-------------------------------------------------");

# Definir las listas de nombres y apellidos
nombres = ["Carlos", "Ana", "Beatriz"];
apellidos = ["García", "López", "Martínez"];

# Ordenar las listas
nombres.sort();
apellidos.sort();

# Mostrar los nombres y apellidos ordenados
print("Nombres ordenados:");
for nombre in nombres:
    print(nombre);

print("\nApellidos ordenados:");
for apellido in apellidos:
    print(apellido);
    
print("--------------------------------------------------");

# Crear una lista para almacenar los nombres
nombres = [];

# Bucle para agregar nombres
while True:
    nombre = input("Ingrese un nombre: ");
    nombres.append(nombre);
    
    # Preguntar si desea agregar otro nombre
    continuar = input("¿Desea agregar otro nombre? (si/no): ").lower();
    if continuar in ["no", "nO", "No", "NO"]:
        break

# Imprimir la lista de nombres ingresados
print("\nLista de nombres ingresados:", nombres);

# Eliminar el nombre con la menor cantidad de caracteres
if nombres:
    nombre_menor = min(nombres, key=len);
    nombres.remove(nombre_menor);

# Imprimir la lista de nombres después de eliminar el nombre con menos caracteres
print("\nLista de nombres después de eliminar el nombre con menos caracteres:", nombres);


