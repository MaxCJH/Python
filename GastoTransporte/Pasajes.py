'''
Nombre del archivo: Game.py
Autor: Max Carlos
Fecha de creación: 19/02/2023
'''
Lunes = int(input("Ingrese el pasaje del Lunes: "))
Martes = int(input("Ingrese el pasaje del Martes: "))
Miercoles = int(input("Ingrese el pasaje del Miércoles: "))
Jueves = int(input("Ingrese el pasaje del Jueves: "))
Viernes = int(input("Ingrese el pasaje del Viernes: "))
Semanas = int(input("Ingrese la cantidad de semanas: "))

PasajeSemanal = Lunes + Martes + Miercoles + Jueves + Viernes
Total = "El pasaje de una semana es: " + str(PasajeSemanal) + " Soles"
print(Total)

TotalMes = "El pasaje de un mes es: " + str(PasajeSemanal * Semanas) + " Soles"
print(TotalMes)

