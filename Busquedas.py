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