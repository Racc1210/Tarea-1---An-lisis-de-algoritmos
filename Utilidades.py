import random

def crearLista(n):
    """
    Genera una lista de tamaño n con números aleatorios entre 1 y 999.

    Args:
        n (entero): Tamaño de la lista.

    Returns:
        lista: Lista de números aleatorios.
    """
    return random.choices(range(1, 1000), k=n)

def crearMatriz(n):
    """
    Genera una matriz de tamaño n x n con números aleatorios entre 1 y 9999.

    Args:
        n (entero): Número de filas y columnas de la matriz.

    Returns:
        lista de listas: Matriz de números aleatorios.
    """
    return [crearLista(n) for i in range(n)]