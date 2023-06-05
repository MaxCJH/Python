'''
Nombre del archivo: Graffiti.py
Autor: Max Carlos
Fecha de creación: 21/06/2022 
'''

##Figuras en Pyton usando el ciclo for
import turtle
max = turtle.Turtle()
max.speed(10)
ventana = turtle.Screen()
ventana.title("Espiral Geométrica con Turtle en Python")
for i in range(180):
    max.forward(200)
    max.right(30)
    max.forward(20)
    max.left(60)
    max.forward(50)
    max.right(30)

    max.penup()
    max.setposition(0,0)
    max.pendown()

    max.right(2)
turtle.done 
