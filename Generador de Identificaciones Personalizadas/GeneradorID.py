'''
Nombre del archivo: GeneradorID.py
Autor: Max Carlos
Fecha de creación: 21/06/2022 
'''

import random

def generar_numero_identificacion():
    # Inicializar una cadena vacía para almacenar el número de identificación generado
    num_identificacion = ""

    # Generar cada dígito del número de identificación
    for i in range(10):
        # Generar un dígito aleatorio entre 0 y 9 y agregarlo a la cadena
        num_identificacion += str(random.randint(0, 9))

    # Devolver el número de identificación generado
    return num_identificacion

# Ejemplo de uso:
print(generar_numero_identificacion())
