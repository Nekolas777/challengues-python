# EJERCICIOS - COMPLEJIDAD ALGORÍTMICA 2024-02

## Reto - 01
### Comparación de Complejidad Temporal entre Búsqueda Lineal y Búsqueda Binaria

**Objetivo:**  
Comparar el tiempo de ejecución de dos algoritmos de búsqueda: búsqueda lineal y búsqueda binaria, y analizar cómo se comportan a medida que aumenta el tamaño de la entrada.

```python
import time
import matplotlib.pyplot as plt

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
```


## Reto - 02
Un ejemplo de un algoritmo de "Búsqueda de clave" mediante fuerza bruta en Python. El
algoritmo genera una clave de cuatro dígitos en el que un digito puede repetirse hasta
máximo dos veces. La regla para generar la clave es: 1) se genera aleatoriamente un
numero base entre 11 y 99, 2) a partir del número anterior se genera el primer digito
usando el operador módulo por 10, 2) el digito 2 se forma del cuadrado del primer digito,
si resulta mayor que 10, se aplica modulo 10, 3) el digito 3 se forma del cuadrado del
segundo digito, si resulta mayor que 10 se aplica modulo 10, 4) el digito 4 se forma del
cuadrado del tercer digito, si resulta mayor que 10, se aplica modulo 10. El programa debe
intentar adivinar la clave generada e indicar la cantidad de intentos. Escribe la solución en
español y detállalo. 
