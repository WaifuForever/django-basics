from typing import List, TypeVar
class Board:
    
    T = TypeVar("T")

    values = []

    # win scenarios
    scenarios = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    
    def __init__(self, values: List[T] ):
        self.values = values
        pass
    
    '''
    it receives an array with 9 positions
    filled with values between 0 and 2.
    it will be treated like a matrix.

    0 1 2
    3 4 5
    6 7 8
    '''
    def is_terminal_state(self, board: List[T]):


        if self.is_board_complete(board):
            return True 
    
        for scenario in self.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == list[scenario[2]]:
                return True
        
        return False

    def is_board_complete(self, board: List[T]):
        for position in board:
            if position == 0:
                return False
        return True

    def evaluate(self, board: List[T], player: T):
        for scenario in self.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                if board[scenario[0]] == player:
                    return 10
                else: 
                    return -10
        return 0

    def minimax(self, board: List[T], depth: int, isMaximizingPlayer: bool, player: T):
        if player == self.values[1]:
            oponent = self.values[2]
        else: 
            oponent = self.values[1]

        score = self.evaluate(board, player)

        if score == 10 or score == -10:
            return score
    
        if self.is_board_complete(board) :
            return 0
        
        if isMaximizingPlayer:
            best = -1000 
            for cell in board :
                if cell == self.values[0]:
                    cell = player
                    best =  max(best, self.minimax(board, depth + 1, not isMaximizingPlayer))
                    cell = self.values[0]
               
            return best

        else :
            best = 1000 
            for cell in board :
                if cell == self.values[0]:
                    cell = oponent
                    best =  min(best, self.minimax(board, depth + 1, not isMaximizingPlayer))
                    cell = self.values[0]
               
            return best

    def best_move(self, board: List[int], player: T):
        bestVal = -1000
        bestMove = -1
        for cell in board :
            moveVal = self.minimax(board, 0, False, player)
            cell = self.values[0]
            if moveVal > bestVal:
                bestMove = cell
                bestVal = moveVal

        return bestMove