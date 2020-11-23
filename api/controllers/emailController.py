from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os

api = Namespace("email")
api_key = os.getenv("API_KEY")
url = 'https://www.googleapis.com/civicinfo/v2/representatives'

@api.route("/all/<int:zip>")    #get all representatives (including national level)
class emailAll(Resource):

    def get(self,zip):
        response = requests.get(f"{url}?address={zip}&fields=officials&key={api_key}")
        return response.json()

@api.route("/state/<int:zip>")  #get all state level representatives
class emailState(Resource):

    def get(self,zip):
        response = requests.get(f"{url}?address={zip}&levels=administrativeArea1&fields=officials&key={api_key}")
        return response.json()

@api.route("/county/<int:zip>") #get all county representatives
class emailCounty(Resource):

    def get(self,zip):
        response = requests.get(f"{url}?address={zip}&levels=administrativeArea2&fields=officials&key={api_key}")
        return response.json()

@api.route("/city/<int:zip>")   #get all city representatives
class emailCity(Resource):

    def get(self,zip):
        response = requests.get(f"{url}?address={zip}&levels=locality&fields=officials&key={api_key}")
        return response.json()
