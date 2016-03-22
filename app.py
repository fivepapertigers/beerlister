from flask import Flask
from flask import render_template
from flask import make_response
from flask import jsonify
from flask import request
from flask_bootstrap import Bootstrap
import db.database as db
import re


app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET'])
def home_page(): 
  return render_template('index.html')

# API ROUTES

# 
@app.route('/api/beers', methods=['GET'])
def list_beers():
  return api_response({'beers': db.get_all_beers()})

# Save beer
@app.route('/api/beers', methods=['POST'])
def save_beer():
  beer_values = nested_form_data('beer', request.values)
  beer = {'beer': db.save_new_beer(beer_values)}
  return api_response(beer)

# Save beer
@app.route('/api/beers/<int:beer_id>', methods=['DELETE'])
def delete_beer(beer_id):
  beers = {'beer': db.delete_beer(beer_id)}
  return api_response(beers)





def api_response(data):
  json = jsonify(data)
  response = make_response(json)
  response.mimetype = 'application/json'
  return response


def nested_form_data(form_name, form_data):
  output = {}
  for key in form_data:
    if (form_name in key):
      match = re.search("\[(.*)\]", key)
      if match:
        output[match.group(1)] = form_data[key]
  return output




if __name__ == '__main__':
  app.debug = True
  app.run()