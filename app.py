from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    # URL del archivo JSON
    url = "https://raw.githubusercontent.com/marto-nieto-g16/Api-Pokemon/main/pokemon-list.json"
    response = requests.get(url)

    if response.status_code == 200:
        # Cargar el contenido JSON
        pokemon_data = json.loads(response.text)
        return render_template('index.html', pokemon_data=pokemon_data)
    else:
        return "Error al cargar el archivo JSON."


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=4001)
