from flask_restx import Api
from api.controllers.issueController import api as ic

api = Api(
    title='environmental-codefest-api',
    version='1',
    description='api for our environmental codefest project'
)

api.add_namespace(ic)
