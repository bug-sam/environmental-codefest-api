from flask import request
from flask_restx import Namespace, Resource, fields

from api.services.issue_service import get_all_issues, save_new_issue


api = Namespace("issues")

@api.route("/")
class IssueList(Resource):

    def get(self):
        return [
            issue.serialize() for issue in get_all_issues()
        ]
    
    def post(self):
        data = request.json
        return save_new_issue(data).serialize()
