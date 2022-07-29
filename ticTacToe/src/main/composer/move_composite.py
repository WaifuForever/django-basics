from src.controllers import MoveController
from src.application.services import MoveService
def register_move_controller() -> MoveController:
    """Composing Register move Controller"""
    service = MoveService
    controller = MoveController(service)

    return controller