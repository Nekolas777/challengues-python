
"""
    Combina los subarreglos ordenados y cuenta los pares que suman el valor objetivo.
    
    :param left: Subarreglo izquierdo ordenado.
    :param right: Subarreglo derecho ordenado.
    :param target: Valor objetivo de la suma.
    :return: Cantidad de pares y lista de los pares que cumplen la condición.
"""
def merge_count(left: int, right: int, target: int) -> tuple:
    
    #inicializamos los indices para recorrer los dos subarreglos "left"y "right"
    i, j = 0, len(right) - 1
    #contador de pares que complen la condicion
    count = 0
    #lista para almecenar los pares encontrados
    pairs = []

    # iteramos mientras los indices esten dentro de los limites del subarreglo
    while i < len(left) and j >= 0:
        # si la suma de los elementos es igual al "valor objetivo" 
        # agregamos a la lista de pares en el arreglo y sumamos el contador de pares
        if left[i] + right[j] == target:
            pairs.append((left[i], right[j]))
            count += 1
            # avanzamos al sigueinte elemento del subarreglo "left"
            i += 1
            # avanzamos al sigueinte elemento del subarreglo "right"
            j -= 1
        # si la suma es menor al valor objetivo avazamos al sig elemento en el subarreglo "left"
        elif left[i] + right[j] < target:
            i += 1
        # caso contrario retrocedemos al elemento anterior en el subarreglo "right"
        else:
            j -= 1

    # retornamos el conteo de pares y la lista de pares encontrados
    return count, pairs


"""
    dividimos el arreglo en subarreglos para aplicar la técnica "divide y vencerás",
    esta funcion se ejecuta recursivamente hasta que los subsarreglos se reduzcan a menos de dos elementos
    donde ya no hay pares para seguir el conteo
    
    :param arr: Arreglo de valores de sensores.
    :param target: Valor objetivo de la suma de pares.
    :return: Cantidad total de pares y lista de los pares encontrados.
"""
def divide_and_conquer(arr: list[int], target: int) -> tuple:
    # caso base: si el arreglo tiene menos de dos elementos, no hay pares, retornamos 0 y una lista vacia
    if len(arr) < 2:
        return 0, []

    # dividimos el arreglo en dos subarreglos mas pequeños para aplicar la técnica
    mid = len(arr) // 2

    # "left" contiene todos los elementos desde el primer elemento hasta el "mid"
    left = arr[:mid]
    # "right" contiene todos los elementos desde "mid" hasta el ultimo elemento
    right = arr[mid:]

    # contamos los pares en el subarreglo "left", que corresponde a la primera mitad del arreglo original.
    # se llama recursivamente a la función para encontrar y contar los pares que cumplen la condición.
    left_count, left_pairs = divide_and_conquer(left, target)

    # contamos los pares en el subarreglo "right", que corresponde a la segunda mitad del arreglo original.
    # se llama recursivamente a la función para encontrar y contar los pares que cumplen la condición.
    right_count, right_pairs = divide_and_conquer(right, target)

    # ordenamos los subsarreglos para hacer la "combinacion" de manera eficiente
    left.sort()
    right.sort()

    # llamamos a la funcion para contar los pares combinando los subarreglos
    merge_count_result, merge_pairs = merge_count(left, right, target)

    # sumamos todos los conteos y combinamos los pares encontrados
    total_count = left_count + right_count + merge_count_result
    total_pairs = left_pairs + right_pairs + merge_pairs

    # retornamos el total de conteos, y los pares encontrados que sumando dan como resultado el "valor objetivo"
    return total_count, total_pairs


"""
    funcion principal que invoca la lógica de divide y vencerás para contar los pares que suman el valor objetivo.
  
    :param arr: Arreglo de valores de sensores.
    :param target: Valor objetivo de la suma de pares.
    :return: Cantidad de pares y lista de tuplas de los pares que cumplen la condición.
"""
def find_pair_values(target: int, arr_sensors: list[int] ) -> list[tuple]:

  # llamamos a la funcion con los parametros aplicando la técnica de divide y vencerás
  return divide_and_conquer(arr_sensors, target)


# caso de prueba propuesto
sensors_values = [1, 5, 7, -1, 6, 3, 4, 2]
target_value = 6

# declaramos la tupla que contendra los resultados
count, pairs = find_pair_values(target_value, sensors_values)

# impresion de los resultados
print(f"Cantidad de pares que suman {target_value} es: {count}")
print("Los pares de sensores son:", pairs)



