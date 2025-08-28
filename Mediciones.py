import time
import tracemalloc


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


def medir_busqueda(algoritmo, matriz, objetivo):
    """
    Mide el tiempo de ejecución y el uso de memoria pico al buscar un elemento en una matriz con el
    algoritmo dado.

    Args:
        algoritmo (funcion): Algoritmo de búsqueda a aplicar.
        matriz (lista de listas): Matriz donde se realiza la búsqueda.
        objetivo (entero): Elemento a buscar.

    Returns:
        tupla: Tiempo de ejecución en segundos y memoria pico en kilobytes (KB).
    """
    tracemalloc.start()
    inicio = time.perf_counter()
    algoritmo(matriz, objetivo)
    fin = time.perf_counter()
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tiempo = fin - inicio
    return tiempo, memoria_pico / 1024 