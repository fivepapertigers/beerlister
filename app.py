from flask import Flask
from flask import render_template
from flask import make_response
from flask import jsonify
from flask import request
from flask.ext.api import status
from flask_bootstrap import Bootstrap
import db.database as db
import re


app = Flask(__name__)
app.url_map.strict_slashes = False
Bootstrap(app)

@app.route('/', methods=['GET'])
def home_page(): 
  return render_template('index.html')

# API ROUTES

# 
@app.route('/api/beers', methods=['GET'])
def list_beers():
  return api_success({'beers': db.get_all_beers()})

# Save beer
@app.route('/api/beers', methods=['POST'])
def save_beer():
  beer_values = request.get_json()['beer']
  result = db.save_new_beer(beer_values)
  if 'error' in result.keys():
    return api_error(result['error'])
  else:
    return api_success({'beer': result['beer']})

# Save beer
@app.route('/api/beers/<int:beer_id>', methods=['DELETE'])
def delete_beer(beer_id):
  beers = {'beer': db.delete_beer(beer_id)}
  return api_success(beers)




def api_success(data):
  json = jsonify(data)
  return api_response(json, status.HTTP_200_OK)

def api_error(message):
  json = jsonify({'error': message})
  return api_response(json, status.HTTP_400_BAD_REQUEST)

def api_response(data, status_code):
  response = make_response(data)
  response.mimetype = 'application/json'
  return response, status_code

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