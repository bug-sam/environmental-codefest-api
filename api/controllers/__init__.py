from flask_restx import Api
from api.controllers.issueController import api as ic
from api.controllers.emailController import api as ec 

api = Api(
    title='environmental-codefest-api',
    version='1',
    description='api for our environmental codefest project'
)

api.add_namespace(ic)
api.add_namespace(ec)
