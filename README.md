# Pokedex-Py

Este proyecto utiliza Flask para mostrar una lista de Pokémon utilizando datos almacenados en formato JSON.

## Descripción

Este proyecto utiliza Flask, un marco de trabajo para aplicaciones web en Python, para mostrar una lista de Pokémon utilizando datos almacenados en formato JSON. Al acceder a la página principal de la aplicación, se mostrará una tabla que contiene información de cada uno de los Pokémon, incluyendo su nombre, número de Pokédex y tipo.

Los datos se cargan de un archivo JSON ubicado en la carpeta `static/data_pokemon/pokemon-list.json`. La función `Load_JSON()` se encarga de leer el archivo y convertirlo en un objeto Python que puede ser utilizado por la aplicación para mostrar la información en la página web.

## Instalación

Para instalar las dependencias del proyecto, es necesario utilizar pip, un administrador de paquetes para Python. En una terminal, ejecute el siguiente comando:

```
pip install Flask
```

Después de instalar Flask, clone el repositorio de GitHub en su computadora utilizando el siguiente comando:

```
git clone https://github.com/marto-nieto-g16/Pokedex-Py.git
```

Reemplace `your-username` y `your-project` con su nombre de usuario de GitHub y el nombre del proyecto, respectivamente.

## Uso

Para ejecutar la aplicación, abra una terminal y navegue hasta la carpeta raíz del proyecto. Ejecute el siguiente comando:

```
python app.py
```

Esto iniciará el servidor de Flask y la aplicación estará disponible en `http://localhost:5000/`. Si desea acceder a la aplicación desde otra computadora en la misma red, cambie `localhost` por la dirección IP de la computadora que está ejecutando el servidor.
