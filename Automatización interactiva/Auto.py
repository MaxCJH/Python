'''
Nombre del archivo: Auto.py
Autor: Max Carlos
Fecha de creación: 04/06/2022
'''

# Aquí comienza el código del script...

import pyautogui
import time

# Esperar unos segundos antes de comenzar la automatización
time.sleep(5)

# Obtener la posición actual del mouse
x, y = pyautogui.position()

# Mover el mouse a una nueva posición
pyautogui.moveTo(x + 100, y + 100, duration=1.0)

# Hacer clic en la nueva posición
pyautogui.click()

# Escribir un mensaje en el teclado
pyautogui.typewrite("Hola, mundo!")

# Presionar la tecla Enter
pyautogui.press("enter")

# Capturar una captura de pantalla
pyautogui.screenshot("captura.png")

# Desplazarse hacia abajo en la página
pyautogui.scroll(100)

# Esperar 4 segundos
time.sleep(4)

# Cerrar la ventana actual
pyautogui.hotkey("alt", "f4")
