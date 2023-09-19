lista1 = [
    [0,0,0],
    [4,5,6],
    [7,8,9]
    ]

lista2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

#for elemento in lista1:
 #   print(elemento)
 
 
# Crear una matriz vacía para almacenar la suma

resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Realizar la suma de las matrices
for i in range(4):
    for j in range(11):
        resultado = i*j
        print(resultado)

# Imprimir la matriz resultante
for fila in resultado:
    print(fila)