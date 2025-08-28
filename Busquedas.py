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

# --- Algoritmos de Búsqueda ---
def busqueda_lineal_matriz(matriz, objetivo):
    """
    Busca un elemento en una matriz usando búsqueda lineal.

    Args:
        matriz (lista de listas): Matriz donde se realiza la búsqueda.
        objetivo (entero): Elemento a buscar.

    Returns:
        bool: True si el elemento se encuentra, False en caso contrario.
    """
    for fila in matriz:
        for elemento in fila:
            if elemento == objetivo:
                return True
    return False

def busqueda_binaria_lista(lista, objetivo):
    """
    Busca un elemento en una lista ordenada usando búsqueda binaria.

    Args:
        lista (lista): Lista ordenada donde se realiza la búsqueda.
        objetivo (entero): Elemento a buscar.

    Returns:
        bool: True si el elemento se encuentra, False en caso contrario.
    """
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False

def busqueda_binaria_matriz(matriz, objetivo):
    """
    Busca un elemento en una matriz, aplicando búsqueda binaria en cada fila.

    Args:
        matriz (lista de listas): Matriz donde se realiza la búsqueda (cada fila debe estar ordenada).
        objetivo (entero): Elemento a buscar.

    Returns:
        bool: True si el elemento se encuentra, False en caso contrario.
    """
    for fila in matriz:
        if busqueda_binaria_lista(fila, objetivo):
            return True
    return False

def encontrar_posicion_matriz(matriz, objetivo):
    """
    Imprime la posición (fila y columna) del elemento objetivo en la matriz, si existe.

    Args:
        matriz (lista de listas): Matriz donde se busca el elemento.
        objetivo (entero): Elemento a buscar.

    Returns:
        None
    """
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            if elemento == objetivo:
                print(f"Encontrado en fila {i}, columna {j}")
                return
    print("No encontrado")

# --- Mediciones ---
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

# --- Pruebas ---
def probar_busquedas():
    tamanos = [10, 100, 500]
    algoritmos = {
        "Lineal": busqueda_lineal_matriz,
        "Binaria": busqueda_binaria_matriz
    }
    objetivo = 128
    for n in tamanos:
        matriz = crearMatriz(n)
        print(f"\nTamaño de matriz: {n}x{n}")
        for nombre, algoritmo in algoritmos.items():
            if nombre == "Binaria":
                matriz_ordenada = [sorted(fila) for fila in matriz]
                tiempo, memoria = medir_busqueda(algoritmo, matriz_ordenada, objetivo)
            else:
                tiempo, memoria = medir_busqueda(algoritmo, matriz, objetivo)
            print(f"{nombre}: Tiempo = {tiempo:.6f} s, Memoria pico = {memoria:.2f} KB")

def probar_busquedas_promedio():
    tamanos = [10, 100, 500]
    algoritmos = {
        "Lineal": busqueda_lineal_matriz,
        "Binaria": busqueda_binaria_matriz
    }
    repeticiones = 5
    objetivo = 128
    for n in tamanos:
        print(f"\nTamaño de matriz: {n}x{n}")
        for nombre, algoritmo in algoritmos.items():
            tiempos = []
            memorias = []
            ultima_matriz = None
            for _ in range(repeticiones):
                matriz = crearMatriz(n)
                if nombre == "Binaria":
                    matriz_ordenada = [sorted(fila) for fila in matriz]
                    tiempo, memoria = medir_busqueda(algoritmo, matriz_ordenada, objetivo)
                    ultima_matriz = matriz_ordenada
                else:
                    tiempo, memoria = medir_busqueda(algoritmo, matriz, objetivo)
                    ultima_matriz = matriz
                tiempos.append(tiempo)
                memorias.append(memoria)
            tiempo_promedio = sum(tiempos) / repeticiones
            memoria_promedio = sum(memorias) / repeticiones
            print(f"{nombre}: Tiempo promedio = {tiempo_promedio:.6f} s, Memoria promedio = {memoria_promedio:.2f} KB")
        encontrar_posicion_matriz(ultima_matriz, objetivo)

print("Búsquedas:")
print("-------------------")
print("Prueba única de búsquedas:")
probar_busquedas()
print("\nPrueba promedio de búsquedas:")
probar_busquedas_promedio()