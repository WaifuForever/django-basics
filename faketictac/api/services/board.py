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
            if position == self.values[0]:
                return False
        return True

    def evaluate(self, board: List[T]):
        for scenario in self.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                if board[scenario[0]] == self.values[1]:
                    return 10
                else: 
                    return -10
        return 0

    def minimax(self, board: List[T], depth: int, isMaximizingPlayer: bool):
        score = self.evaluate(board)
        print(board)
        if score == 10 or score == -10:
            return score
    
        if self.is_board_complete(board):
            return 0
        
        if isMaximizingPlayer:
            best = -1000 
            for i in range(0,8) :
                if board[i] == self.values[0]:
                    board[i] = self.values[1]
                    best = max(best, self.minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i] = self.values[0]
               
            return best

        else :
            best = 1000 
            for i in range(0,8) :
                if board[i] == self.values[0]:
                    board[i] = self.values[2]
                    best = min(best, self.minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i] = self.values[0]
               
            return best

    def best_move(self, board: List[T]):
        bestVal = -1000
        bestMove = -1
        for i in range(0,8) :
            if board[i] == self.values[0]:
                
                board[i] = self.values[1]
                
                moveVal = self.minimax(board, 0, False)
                
                board[i] = self.values[0]
                if moveVal > bestVal:
                    bestMove = i
                    bestVal = moveVal
                    print(bestVal)
        
        return bestMove