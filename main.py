from Ordenamientos import quicksort, mergesort
from Busquedas import busqueda_lineal_matriz, busqueda_binaria_matriz, encontrar_posicion_matriz
from Utilidades import crearLista, crearMatriz
from Mediciones import medir_ordenamiento, medir_busqueda




def probar_promedio_algoritmos():
    tamanos = [10, 100, 1000, 10000]
    algoritmos = {
        "Quicksort": quicksort,
        "Mergesort": mergesort
    }
    repeticiones = 100
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



def probar_busquedas():
    tamanos = [10, 100, 500]
    algoritmos = {
        "Lineal": busqueda_lineal_matriz,
        "Binaria": busqueda_binaria_matriz
    }
    objetivo = 128  # Puedes cambiar el valor a buscar
    for n in tamanos:
        matriz = crearMatriz(n)
        print(f"\nTamaño de matriz: {n}x{n}")
        for nombre, algoritmo in algoritmos.items():
            tiempo, memoria = medir_busqueda(algoritmo, matriz, objetivo)
            print(f"{nombre}: Tiempo = {tiempo:.6f} s, Memoria pico = {memoria:.2f} KB")
            #encontrar_posicion_matriz(matriz, objetivo)

def probar_busquedas_promedio():
    tamanos = [10, 100, 500]
    algoritmos = {
        "Lineal": busqueda_lineal_matriz,
        "Binaria": busqueda_binaria_matriz
    }
    repeticiones = 100
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


if __name__ == "__main__":
    # Llama aquí a las funciones de prueba que desees ejecutar
    print("Ordenamientos: \n")
    probar_ordenamientos()
    probar_promedio_algoritmos()
    print("Busquedas: \n")
    probar_busquedas()
    probar_busquedas_promedio()