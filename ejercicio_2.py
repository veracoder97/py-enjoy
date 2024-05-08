#Descripción: Crea un programa que genere los primeros N términos de
#la secuencia de Fibonacci.

# Bienvenida al usuario
print("Bienvenido al programa de generación de la secuencia de Fibonacci.")

# Solicitar al usuario que ingrese el número de términos a generar que sea positivo y no decimal
while True:
    try:
        n = int(input("Por favor, introduce el número de términos de la secuencia de Fibonacci que deseas generar (debe ser un número entero positivo): "))
        if n <= 0:
            print("Error: Debes ingresar un número entero positivo.")
        else:
            break
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")
# Inicializar los primeros dos términos de la secuencia
fibonacci = [0, 1]

# Generar la secuencia de Fibonacci
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

# Mostrar la secuencia generada
print("Los primeros {} términos de la secuencia de Fibonacci son: {}".format(n, fibonacci))
