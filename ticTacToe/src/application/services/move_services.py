from typing import List
from src.application.domain.models import GameModel

class MoveService:
    # win scenarios
    scenarios = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    @classmethod
    async def best_move(cls, request):
        game = GameModel(**request.json)
        bestVal = -1000
        bestMove = -1
        
        for i in range(0,8) :
            if game.board[i] == game.values[0]:
                print(game.board[i])
                game.board[i] = game.values[1]
                
                moveVal = cls.minimax(game.board, 0, False, game.values)
                
                game.board[i] = game.values[0]
                if moveVal > bestVal:
                    bestMove = i
                    bestVal = moveVal
                    print(bestVal)
        
        return bestMove

    @classmethod
    def is_terminal_state(cls, board: List[int]):

        if cls.is_board_complete(board):
            return True 
    
        for scenario in cls.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                return True
        
        return False

    @classmethod
    def is_board_complete(cls, board: List[int], values: List[int]):
        for position in board:
            if position == values[0]:
                return False
        return True

    @classmethod
    def evaluate(cls, board: List[int], values: List[int]):
        for scenario in cls.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                if board[scenario[0]] == values[1]:
                    return 10
                else: 
                    return -10
        return 0
    
    @classmethod
    def minimax(cls, board: List[int], depth: int, isMaximizingPlayer: bool, values: List[int]):
        score = cls.evaluate(board, values)
        
        if score == 10 or score == -10:
            return score
    
        if cls.is_board_complete(board, values):
            return 0
        
        if isMaximizingPlayer:
            best = -1000 
            for i in range(0,8) :
                if board[i] == values[0]:
                    board[i] = values[1]
                    best = max(best, cls.minimax(board, depth + 1, not isMaximizingPlayer, values))
                    board[i] = values[0]
               
            return best

        else :
            best = 1000 
            for i in range(0,8) :
                if board[i] == values[0]:
                    board[i] = values[2]
                    best = min(best, cls.minimax(board, depth + 1, not isMaximizingPlayer, values))
                    board[i] = values[0]
               
            return best
