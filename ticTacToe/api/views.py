from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.services.board import Board


@api_view(['GET'])
def getBestMove(request):
    board =  Board(request.data.get('values'))
    board.best_move(request.data.get('board'), request.data.get('player'))
    return Response()


