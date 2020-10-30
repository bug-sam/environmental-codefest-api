from flask_restx import Namespace, Resource

from api.services.issue_service import get_all_issues


api = Namespace("issues")

@api.route("/")
class IssueList(Resource):

    def get(self):
        return get_all_issues()
