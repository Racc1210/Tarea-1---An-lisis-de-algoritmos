import time
import tracemalloc
import random

#Funcion para generar una matriz del tamaño deseao "nxm", dentro del rango de valores de 0-99.
#Entrada de un numero "n" para filas y un numero "m" para columnas
def generar_matriz(n, m):
    return [[random.randint(0, 99) for _ in range(m)] for _ in range(n)]

#Funcion de busqueda lineal de elementos en una matriz aleatoremente creada
#Entrada de una lista de listas creada aleatoremente con un tamaño nxm definido y un elemento e encontrar dentro de la matriz
def busquedaLineal(lista_de_listas, elemento):
    print("\nMatriz: ", len(lista_de_listas),"x",len(lista_de_listas[0]))
    tracemalloc.start()#Mide la memoria en KB
    inicio = time.time()#Mide el tiempo en S
    
    for i in range(len(lista_de_listas)):
        for j in range(len(lista_de_listas[i])):

            if lista_de_listas[i][j] == elemento:
                fin = time.time()
                memoria_actual, memoria_final = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                
                print("Elemento encontrado en: Fila:", i, "Columna:", j)
                print("Tiempo de ejecucion:", round(fin - inicio, 6), "segundos")
                print("Memoria utilizada:", round(memoria_final / 1024, 2), "KB")
                return (i, j)
    
    fin = time.time()
    memoria_actual, memoria_final = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print("Elemento no encontrado")
    print("Tiempo de ejecución:", round(fin - inicio, 6), "segundos")
    print("Memoria utilizada:", round(memoria_final / 1024, 2), "KB")


#CASOS DE PRUEBAS 10x10 100x100 500x500
n = 500         #Filas 
m = 500         #Columnas
elemento = 1000   #Valor e encontrar entre 0 y 99

matriz = generar_matriz(n, m)
#print(matriz)
busquedaLineal(matriz, elemento)