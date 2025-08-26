import random

def crearLista(n):
    return random.choices(range(1, 255), k=n)


def crearMatriz(n):
    return [crearLista(n) for i in range(n)]

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista)//2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista)//2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])

    return merge(izquierda,derecha)

def merge(izquierda,derecha):
    res = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            res.append(izquierda[i])
            i += 1
        else:
            res.append(derecha[j])
            j += 1
    res.extend(izquierda[i:])
    res.extend(derecha[j:])
    return res




def pruebas(n):
    matriz = crearMatriz(n)
    matriz_quicksort = matriz.copy()
    matriz_mergesort = matriz.copy()

    print("original: ")
    print(matriz)
    print("\n")

    print("quicksort: ")
    print(matriz_quicksort)
    print("\n")
    for i in range(n):
        matriz_quicksort[i] = quicksort(matriz_quicksort[i])

    print("mergesort: ")
    print(matriz_mergesort)
    print("\n")
    for i in range(n):
        matriz_mergesort[i] = mergesort(matriz_mergesort[i])

    print(matriz_quicksort)
    print("\n")
    print(matriz_mergesort)
    return 0

#print(pruebas(4))
print(quicksort(crearLista(100000)))
#print(crearMatriz(10000))
