from flask_restx import Namespace, Resource

api = Namespace("issues")

@api.route("/")
class IssueList(Resource):

    def get(self):
        return {"hello": "world"}



