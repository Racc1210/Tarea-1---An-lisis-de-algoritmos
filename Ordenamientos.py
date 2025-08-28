def quicksort(lista):
    """
    Ordena una lista usando el algoritmo Quicksort.

    Args:
        lista (lista): Lista de números a ordenar.

    Returns:
        lista: Lista ordenada.
    """
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista)//2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)


def mergesort(lista):
    """
    Ordena una lista usando el algoritmo Mergesort.

    Args:
        lista (lista): Lista de números a ordenar.

    Returns:
        lista: Lista ordenada.
    """
    if len(lista) <= 1:
        return lista
    medio = len(lista)//2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    return merge(izquierda, derecha)



def merge(izquierda, derecha):
    """
    Fusiona dos listas ordenadas en una sola lista ordenada.

    Args:
        izquierda (lista): Primera lista ordenada.
        derecha (lista): Segunda lista ordenada.

    Returns:
        lista: Lista fusionada y ordenada.
    """
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

def quicksort_matriz(matriz):
    """
    Ordena cada fila de una matriz usando el algoritmo Quicksort.

    Args:
        matriz (lista de listas): Matriz a ordenar.

    Returns:
        lista de listas: Matriz con cada fila ordenada.
    """
    for i in range(len(matriz)):
        matriz[i] = quicksort(matriz[i])
    return matriz