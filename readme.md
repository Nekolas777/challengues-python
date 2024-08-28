# EJERCICIOS - COMPLEJIDAD ALGORÍTMICA 2024-02

## [Reto - 01](./reto-01.py)
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


## [Reto - 02](./reto-02.py)
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

## [Reto - 03](./reto-03.py)

Ud. ha sido contratado en una empresa de tecnología que ha desplegado una red de sensores en una ciudad para monitorear la calidad del aire. Cada sensor reporta un valor numérico que representa la calidad del aire en su ubicación. Tu tarea es optimizar la distribución de recursos para mejorar la calidad del aire en la ciudad.

Para ello, necesitas identificar las ubicaciones críticas donde la combinación de dos sensores reporta un valor objetivo que indica una calidad del aire deficiente. Debes contar cuántos pares de sensores reportan valores que suman exactamente el valor objetivo.

Desarrollar un algoritmo que, dado un arreglo de valores de sensores y un valor objetivo, cuente el número de pares de sensores cuyos valores suman exactamente el valor objetivo utilizando la técnica de divide y vencerás.

Se requiere:
- Desarrollar el algoritmo en lenguaje Python (.py o .ipynb).
- Resolver el ejercicio utilizando la técnica divide y vencerás.
- Hallar el número de pares que cumplen la condición dada.
- Mostrar los elementos (pares) que cumplen la condición dada.