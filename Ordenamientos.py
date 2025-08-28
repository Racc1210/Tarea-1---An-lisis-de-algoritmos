import random
import time
import tracemalloc

# --- Utilidades ---
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

# --- Algoritmos de Ordenamiento ---
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


# --- Mediciones ---
def medir_ordenamiento(algoritmo, lista):
    """
    Mide el tiempo de ejecución y el uso de memoria pico al ordenar una lista con el algoritmo dado.

    Args:
        algoritmo (funcion): Algoritmo de ordenamiento a aplicar.
        lista (lista): Lista de números a ordenar.

    Returns:
        tupla: Tiempo de ejecución en segundos y memoria pico en kilobytes (KB).
    """
    tracemalloc.start()
    inicio = time.perf_counter()
    algoritmo(lista.copy())
    fin = time.perf_counter()
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tiempo = fin - inicio
    return tiempo, memoria_pico / 1024  

# --- Pruebas ---
def probar_ordenamientos():
    tamanos = [100, 1000, 10000, 100000]
    algoritmos = {
        "Quicksort": quicksort,
        "Mergesort": mergesort
    }
    for n in tamanos:
        lista = crearLista(n)
        print(f"\nTamaño de lista: {n}")
        for nombre, algoritmo in algoritmos.items():
            tiempo, memoria = medir_ordenamiento(algoritmo, lista)
            print(f"{nombre}: Tiempo = {tiempo:.6f} s, Memoria pico = {memoria:.2f} KB")

def probar_promedio_algoritmos():
    tamanos = [100, 1000, 10000, 100000]
    algoritmos = {
        "Quicksort": quicksort,
        "Mergesort": mergesort
    }
    repeticiones = 5
    for n in tamanos:
        print(f"\nTamaño de lista: {n}")
        for nombre, algoritmo in algoritmos.items():
            tiempos = []
            memorias = []
            for _ in range(repeticiones):
                lista = crearLista(n)
                tiempo, memoria = medir_ordenamiento(algoritmo, lista)
                tiempos.append(tiempo)
                memorias.append(memoria)
            tiempo_promedio = sum(tiempos) / repeticiones
            memoria_promedio = sum(memorias) / repeticiones
            print(f"{nombre}: Tiempo promedio = {tiempo_promedio:.6f} s, Memoria promedio = {memoria_promedio:.2f} KB")


print("Ordenamientos:")
print("-------------------")
print("Prueba única de ordenamientos:")
probar_ordenamientos()
print("\nPrueba promedio de ordenamientos:")
probar_promedio_algoritmos()