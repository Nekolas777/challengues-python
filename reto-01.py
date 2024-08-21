import timeit
import matplotlib.pyplot as plt

def busqueda_lineal(lista, objetivo):
    
    for i in range(len(lista)):  # 1 + n(1 + INSIDE)
        if lista[i] == objetivo:  # 1 + 1
            return i  # 1
    return -1  # 1

# Worst and Average Case
# 1 + n(1 + 2) + 1 = 1 + 3n + 1 = 3n + 2

# Best Case
# 1 + 1 + 1 = 3


def busqueda_binaria(lista, objetivo):
    
    izquierda, derecha = 0, len(lista) - 1  # 1 + 1
    while izquierda <= derecha:  # log(n) * (1 + INSIDE)
        medio = (izquierda + derecha) // 2  # 1
        if lista[medio] == objetivo:  # 1 + 1
            return medio  # 1
        elif lista[medio] < objetivo:  # 1 + 1
            izquierda = medio + 1  # 1
        else:
            derecha = medio - 1  # 1
    return -1  # 1

# Worst and Average Case
# 2 + log(n) * (1 + 1 + 1 + 1 + 1 + 1) + 1 = 2 + log(n) * 6 + 1 = 6log(n) + 3

# Best Case
# 2 + 1 + 1 + 1 = 5



# Función para medir el tiempo de ejecución
def medir_tiempo(func, lista, objetivo):
    setup_code = f"from __main__ import {func.__name__}, lista, objetivo"
    stmt = f"{func.__name__}(lista, objetivo)"
    times = timeit.repeat(stmt, setup=setup_code, repeat=5, number=1000)
    return min(times)

# Lista de prueba y objetivo
lista = list(range(20000))
objetivo = 10000

# Medir el tiempo de ejecución de ambas funciones
tiempo_lineal = medir_tiempo(busqueda_lineal, lista, objetivo)
tiempo_binaria = medir_tiempo(busqueda_binaria, lista, objetivo)

print(f"Tiempo de búsqueda lineal: {tiempo_lineal:.6f} segundos")
print(f"Tiempo de búsqueda binaria: {tiempo_binaria:.6f} segundos")