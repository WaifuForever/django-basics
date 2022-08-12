from src.main.composer import register_move_controller
from sanic import Blueprint, response
from pydantic import ValidationError

MOVE_ROUTES = Blueprint('move_routes')
move_controller = register_move_controller()


@MOVE_ROUTES.route('/move', methods=['POST'])
async def best_move(request):
    try:
        return await move_controller.best_move(request)
    except ValidationError as err:
        error = err.errors()
        return response.json(
            body={
                "code": 400,
                "message": str(error[0]["msg"]),
                "description": str(err)
            },
            status=400
        )#.json header vem com application/json
        #ErrorHandler.build();

@MOVE_ROUTES.route('/finalState', methods=['POST'])
async def final_state(request):
    try:
        return await move_controller.is_terminal_state(request)
    except ValidationError as err:
        error = err.errors()
        return response.json(
            body={
                "code": 400,
                "message": str(error[0]["msg"]),
                "description": str(err)
            },
            status=400
        )#.json header vem com application/json
        #ErrorHandler.build();