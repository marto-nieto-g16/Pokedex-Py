
from flask import Flask, render_template
import json

app = Flask(__name__)

def Load_JSON():
	with open('static/data_pokemon/pokemon-list.json') as file:
		return json.load(file)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html', pokemon=Load_JSON())


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
