He aquí un borrador para el archivo `README.md` de tu proyecto en Flask:

---

# Pokedex Py

!Pokedex Py

<span>https://github.com/marto-nieto-g16/Pokedex-Py/blob/master/index%20busqueda.png</span><span>)</span>

Pokedex Py es una aplicación web desarrollada en Flask que permite a los usuarios visualizar una lista de Pokémon, junto con sus características y detalles básicos. La aplicación carga los datos de un archivo JSON alojado en un repositorio de GitHub y muestra una interfaz intuitiva para explorar cada Pokémon.

## Funcionalidades

- **Visualización de Pokémon**: Muestra una lista de Pokémon con su número, nombre, tipo, habilidades y otras características.
- **Búsqueda Rápida**: Permite buscar Pokémon por nombre en tiempo real.
- **Detalles en Popup**: Muestra una vista ampliada de los detalles del Pokémon seleccionado mediante un popup.
- **Interfaz Responsable**: Diseño adaptable que se visualiza correctamente en dispositivos móviles y de escritorio.

## Tecnologías

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Datos**: JSON
- **Interactividad**: JavaScript, Muuri.js para filtros

## Estructura del Proyecto

- **app.py**: Archivo principal que ejecuta la aplicación Flask.
- **templates/index.html**: Plantilla HTML que muestra la lista de Pokémon y sus detalles.
- **static/css/estilos.css**: Estilos personalizados para la aplicación.
- **static/js/main.js**: Script JavaScript para la interactividad de la interfaz.
  
## Instalación y Ejecución

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/pokedex-py.git
   ```
   
2. **Instala los paquetes requeridos**:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Ejecuta la aplicación**:
   ```bash
   python app.py
   ```
   
4. Accede a la aplicación en tu navegador en `http://localhost:4001`.

## Uso

1. Navega a la página de inicio para ver la lista de Pokémon.
2. Usa la barra de búsqueda para filtrar Pokémon por su nombre.
3. Haz clic en un Pokémon para ver sus detalles en un popup.

## Fuentes de Datos

- La aplicación utiliza un archivo JSON público de un repositorio de GitHub que contiene los datos de los Pokémon.

## Créditos

Diseñado y desarrollado por [Marto Nieto Guerrero](https://github.com/marto-nieto-g16). Puedes encontrarme en [Twitter](https://twitter.com/marto_nieto)
