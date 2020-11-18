from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os


from api.services.issue_service import get_all_issues, save_new_issue


api = Namespace("email")
api_key = os.getenv("API_KEY")
url = 'https://www.googleapis.com/civicinfo/v2/representatives'

@api.route("/email")
class emailStuff(Resource):

    def get(self):
        response = requests.get(url+"?address=19104&key="+api_key)
        return response.json()



