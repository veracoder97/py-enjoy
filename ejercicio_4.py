#- Descripción: Solicita al estudiante que cree un programa que calcule el
#área de un triángulo dada su base y altura. 

# Bienvenida al usuario
print("Bienvenido al calculador de el área de un triángulo.")

# Solicitar al usuario que ingrese la base del triángulo (debe ser positiva)
while True:
    base = float(input("Por favor, introduce la longitud de la base del triángulo (debe ser un número positivo): "))
    if base>0:
        break
    else:
        print("Error: La base debe ser un número positivo. Intenta nuevamente.")

# Solicitar al usuario que ingrese la altura del triángulo (debe ser positiva)
while True:
    altura = float(input("Ahora, introduce la altura del triángulo (debe ser un número positivo): "))
    if altura > 0:
        break
    else:
        print("Error: La altura debe ser un número positivo. Intenta nuevamente.")
# Calcular el área del triángulo
area = (base * altura)/2

# Mostrar el resultado
print("El área del triángulo con base {} y altura {} es: {}".format(base, altura, area))
