from src.main.routes import MOVE_ROUTES
from sanic import Sanic, response, request

api = Sanic("https")

api.blueprint(MOVE_ROUTES, url_prefix='v1')
@api.route('/', methods=['GET'])
async def index(request):
    return response.json({"message": "Hello World!"})