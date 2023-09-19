# Crear dos matrices de 3x3 llenas de ceros
matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Llenar la primera matriz
print("Llenando la primera matriz:")
for i in range(3):
    for j in range(3):
        valor = float(input(f"Ingresa el valor para la posición [{i}][{j}]: "))
        matriz1[i][j] = valor

# Llenar la segunda matriz
print("Llenando la segunda matriz:")
for i in range(3):
    for j in range(3):
        valor = float(input(f"Ingresa el valor para la posición [{i}][{j}] de la segunda matriz: "))
        matriz2[i][j] = valor

# Imprimir las matrices
print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("Matriz 2:")
for fila in matriz2:
    print(fila)
