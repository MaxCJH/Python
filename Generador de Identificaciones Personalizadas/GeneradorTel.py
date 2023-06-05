'''
Nombre del archivo: GeneradorTel.py
Autor: Max Carlos
Fecha de creación: 21/06/2022 
'''

import random

def generar_numero_identificacion():
    # Inicializar el número de identificación con el primer dígito "9"
    num_identificacion = "9"

    # Generar los siguientes 8 dígitos del número de identificación
    for i in range(8):
        # Generar un dígito aleatorio entre 0 y 9 y agregarlo al número de identificación
        num_identificacion += str(random.randint(0, 9))

    # Devolver el número de identificación generado
    return num_identificacion

# Ejemplo de uso:
print(generar_numero_identificacion())
