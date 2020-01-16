# Pokedex-Py

Es un prototipo de API para la Visualizar Todos los datos de Pokémon que necesitas, es de fácil acceso a través de RESTful moderna desarrollada en Python y bajo el framewok Flask

Estos datos se encuentran se encuentran en formato Json y son obtenidos por python atravez de la funcion json.load; los cuales despues de cargarse muestra la informacion del pokemon

# Datos que Muestra la API 

  * Numero
  * Nombre
  * Tipo
  * Habilidad
  * Entre otras cosas mas

# Requisitos

1. Python 3.x
2. Libreria Flask y JSON
  
  # Librerias y Modulos a Utilizar 
 
 from flask import Flask, render_template
 import json

from flask import Flask y app = Flask(__name__) : Es una funcion de  WSGI que permite obtener la información de la petición, realizar una operación y posteriormente generar una respuesta.

render_template: Es un Modulo de Flask que nos permite Renderizar la informacion obtenida de una metodo o variable y enviarla a una platilla html.

En este Proyecto se utilizo para enviar los datos obtenidos de JSON a la plantilla index.html y mostrar los datos Ordenados en forma de informacion
  
  # Funcion para Cargar un Archivo Json y Obtener Los Datos de Cada Pokemon  
  
  def LoadJson:
    with open('./static/data_pokemon/pokemon-list.json') as file:  -> Se ingresa la ubicacion del archivo el cual desea obtener los                                                                            metadatos
    return json.load(file)   -> Retorna Cada Metadato del archivo
    
@app.route('/')  -> Funcion que permite acceder a index() desde la página principal (‘/‘) y devolver su contenido que simplemente va a devolver
def index():
	return render_template('index.html', pokemon=Load_JSON())
 
# Ejecutar 

Cuando se ejecuta el programa con la función: app.run lo que se hace es ejecutar un servidor web para hacer las pruebas y se puede acceder a él desde cualquier direccion (0.0.0.0) desde el puerto 5000. Además se ha activado la depuración (debug= True),

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  
Para realizar un Test 

python app.py

<p align="center"> <img src="https://github.com/marto-nieto-g16/Pokedex-Py/blob/master/index%20pokedex.png" /> <img src="https://github.com/marto-nieto-g16/Pokedex-Py/blob/master/index%20busqueda.png" /> </p> 
