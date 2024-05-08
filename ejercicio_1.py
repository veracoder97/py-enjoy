#Ejercicio 1: Contar Vocales en una Cadena
#- Descripción: Pide al estudiante que desarrolle un programa que cuente
#el número de vocales en una cadena dada.
#- Pensamiento Lógico: Identificar y contar vocales.
#- Pseudocódigo: Describe el proceso de conteo de vocales.
#- Diagrama de Flujo: Visualiza el flujo de decisión para contar vocales.
#- Python: Implementa el programa en Python. 


# Bienvenida al usuario
print("Bienvenido al contador de vocales.")
nombre = input("Por favor, introduce tu nombre: ")

# Pedir al usuario que introduzca la cadena de texto
texto = input("Hola {}, por favor introduce una cadena de texto: ".format(nombre))

# Inicializar contadores para vocales abiertas y cerradas
vocales_abiertas = 0
vocales_cerradas = 0
vocales_totales = 0

# Lista de vocales abiertas y cerradas
vocales_abiertas_list = ['a', 'e', 'o']
vocales_cerradas_list = ['i', 'u']

# Iterar sobre cada letra en el texto y contar las vocales
for letra in texto:
    if letra.lower() in vocales_abiertas_list:
        vocales_abiertas += 1
    elif letra.lower() in vocales_cerradas_list:
        vocales_cerradas += 1
    if letra.lower() in ('a','e','i','o','u'):
        vocales_totales += 1    

# Mostrar los resultados
print("\nNombre: ", (nombre))
print("Este es el texto introducido: ", (texto))
print("Número de vocales abiertas: ", (vocales_abiertas))
print("Número de vocales cerradas: ", (vocales_cerradas))
print("Número de vocales toales : ", (vocales_totales))