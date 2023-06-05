'''
Nombre del archivo: Sueldo.py
Autor: Max Carlos
Fecha de creación: 11/04/2023
'''

# Aquí comienza el código del script...


# Pedir al usuario que ingrese sueldo mensual y número de días y horas trabajadas
sueldo_mensual = float(input("Ingrese su sueldo mensual: "))
dias_trabajados = int(input("Ingrese el número de días trabajados: "))
horas_diarias = float(input("Ingrese el número de horas trabajadas por día: "))

# Calcular el salario por día y por hora
salario_diario = sueldo_mensual / dias_trabajados
salario_hora = salario_diario / horas_diarias

# Imprimir los resultados
print("Salario diario: S/." + str(round(salario_diario, 2)))
print("Salario por hora: S/." + str(round(salario_hora, 2)))
