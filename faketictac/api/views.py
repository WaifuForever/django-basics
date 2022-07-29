from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.services.board import Board

@api_view(['GET'])
def hello_world(request):
    
    return Response( {'message': "Hello World"})


@api_view(['POST'])
def getBestMove(request):
    board = Board(request.data.get('values'))
    data = {'data': board.best_move(request.data.get('board'))}
    return Response(data)

@api_view(['POST'])
def testEvaluate(request):
    board = Board(request.data.get('values'))
    data = {'result': board.evaluate(request.data.get('board'))}
    return Response(data)

@api_view(['POST'])
def testMinimax(request):
    board = Board(request.data.get('values'))
    data = {'result': board.minimax(request.data.get('board'), 0, False)}
    return Response(data)

@api_view(['POST'])
def testIsBoardComplete(request):
    board = Board(request.data.get('values'))
    data = {'result': board.is_board_complete(request.data.get('board'))}
    return Response(data)

@api_view(['POST'])
def testIsTerminal(request):
    board = Board(request.data.get('values'))
    data = {'result': board.is_terminal_state(request.data.get('board'))}
    return Response(data)
