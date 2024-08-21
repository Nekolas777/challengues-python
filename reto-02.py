import random

#funcion para generar la llave en base a las condiciones
def generate_key() -> int:
  # volvemos a generar la llave secreta hasta que se cumpla la condicion que no puede
  # haber mas de dos numeros repetidos
  while True:
    #generamos el numero aleatorio
    random_number = random.randint(11, 99)

    # sacamos el modulo x 10 para hallar el primer digito
    first_digit = random_number % 10
    # invocamos a la funcion para generar el segundo, tercer y cuarto digito
    second_digit = elevate_number(first_digit)
    third_digit = elevate_number(second_digit)
    fourth_digit = elevate_number(third_digit)

    # lo manejamos como un arreglo de numeros
    digits = [first_digit, second_digit, third_digit, fourth_digit]
    print(digits)

    # verifica si cada digito a aparecido como maximo 2 veces
    if all(digits.count(d) <= 2 for d in digits):
      # hacemos el join de los numeros para formar la clave
      secret_key = int(f"{first_digit}{second_digit}{third_digit}{fourth_digit}")
      # finalmente retornamos la llave secreta
      return secret_key
    
# creamos una funcion para elevar el numero y validar si es que es mayor a 10 que aplique modulo 10
def elevate_number(number: int) -> int:

  #elevamos el numero al cuadrado
  number_square = pow(number, 2)

  # si el numero es mayor a 10 saca el modulo por 10
  if(number_square > 10):
    return number_square % 10

  return number_square

# Este algoritmo de fuerza bruta garantiza que se probarán todas las combinaciones posibles de cuatro dígitos 
# hasta encontrar la clave secreta, y retornará número de intentos
def brute_force_algorithm(secret_key: int) -> int:
    attempts = 0

    for i in range(10000):  # recorremos en el intervalo dado (4 dígitos de 0000 - 9999)
        attempts += 1
        # verificamos si el numero es igual a la llave secreta y retornamos el numero de intentos realizados
        if i == secret_key:
            return attempts
        
    return attempts

# generamos la clave secreta
secret_key = generate_key()
print(f"clave generada: {secret_key}")

# buscamos la clave usando el algoritmo de fuerza bruta
attempts = brute_force_algorithm(secret_key)
print(f"clave encontrada luego de {attempts} intentos")
