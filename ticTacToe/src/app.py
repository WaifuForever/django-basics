from src.main.routes import MOVE_ROUTES
from sanic import Sanic, response, request

from src.utils.options import setup_options
from src.utils.cors import add_cors_headers

api = Sanic("https")

api.blueprint(MOVE_ROUTES, url_prefix='v1')
@api.route('/', methods=['GET'])
async def index(request):
    return response.json({"message": "Hello World!"})

# Add OPTIONS handlers to any route that is missing it
api.register_listener(setup_options, "before_server_start")

# Fill in CORS headers
api.register_middleware(add_cors_headers, "response")
 