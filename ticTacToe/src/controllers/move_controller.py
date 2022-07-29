#import services
from sanic import response
from http import HTTPStatus

from typing import Optional, Tuple


class MoveController:
    def __init__(self, service):
        self.service = service
    
    async def best_move(
        self, request=None
    ) -> Tuple[Optional[dict], HTTPStatus]:
        result = await self.service.best_move(request)

        return response.json(body=result, status=HTTPStatus.OK)
