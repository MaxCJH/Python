'''
Nombre del archivo: Flask.py
Autor: Max Carlos
Fecha de creación: 02/06/2022 
'''

from flask import Flask, render_template, url_for
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    # Establecer la conexión con la base de datos
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="AQwd0g8?i&PXA57!eds1agpTbOn#VXh8LLZ3DqXp",
        database="bd_sistema_ventas"
    )

    if myDB:
        # Crear un cursor para ejecutar consultas SQL
        cursor = myDB.cursor(dictionary=True)

        # Ejecutar una consulta para seleccionar registros de la tabla "trabajadores" donde el sueldo sea mayor a 350,000
        cursor.execute("SELECT * FROM trabajadores WHERE sueldo > '350000'")

        # Obtener todos los registros devueltos por la consulta
        registros = cursor.fetchall()

        # Renderizar la plantilla 'index.html' y pasar los datos de los registros como parámetro
        return render_template('index.html', data=registros)
    else:
        # Si no se puede establecer la conexión con la base de datos, mostrar un mensaje de error
        return "Error en la conexión a la base de datos"

if __name__ == "__main__":
    # Ejecutar la aplicación Flask en modo de depuración y en el puerto 8000
    app.run(debug=True, port=8000)
