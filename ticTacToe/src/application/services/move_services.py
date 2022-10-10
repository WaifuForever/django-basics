from typing import List, TypeVar
from random import randint
from src.application.domain.models import GameModel

T = TypeVar("T")

class MoveService:
    # win scenarios
    scenarios = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    values = []
    current_player = -1

    @classmethod
    def find_winner(self, game: GameModel):
        winner = 0
        for scenario in self.scenarios:
            if game.board[scenario[0]] == game.board[scenario[1]] and game.board[scenario[1]] == game.board[scenario[2]]:
                if game.board[scenario[0]] != game.values[0]:
                    if game.board[scenario[0]] == game.values[1]:
                        winner += 1 # first player won
                    else:
                        winner += 2 # second player won
        if(winner > 2):
            return -1
            
        return winner
        

    @classmethod
    async def is_terminal_state(self, request) -> int:
        game = GameModel(**request.json)
        
        if len(game.board) != 9:
            return -1
      
        n1 = game.board.count(game.values[1])
        n2 = game.board.count(game.values[2])

        if not (n1 == n2 or n1 + 1 == n2 or n2 + 1 == n1):
            return -1 # invalid board
        
        winner = self.find_winner(game)
        print(winner)
        if(winner == 0):
            if self.is_board_complete(game.board, game.values):
                return 0 # draw
            else: 
                return 3 # incomplete board
        else:
            return winner
       


    @classmethod
    async def best_move(self, request):
        game = GameModel(**request.json)
        bestVal = -1000000
        bestMove = -1
        self.values = game.values
        moves =  []
        #base case
        if self.is_board_empty(game.board):
            return {
                0: 0,
                1: 2,
                2: 4,
                3: 6,
                4: 8

            }[randint(0, 4)]

        self.current_player = self.whose_turn(game.board, game.values)

        if self.current_player == -1:
            return -1   

        #print(game.board, self.values[self.current_player])
        
        for i in range(0,9) :
            #print("%d == %d - %r" % (game.board[i], game.values[0], game.board[i] == game.values[0]))
            if game.board[i] == self.values[0]:
                game.board[i] = self.values[self.current_player]
                #print()
                #print(game.board, "[%d]" % (i))
                moveVal = self.minimax(game.board, 0, False)
                
                moves.append((i, int(moveVal)))
                game.board[i] = self.values[0]
                if moveVal > bestVal:
                    bestMove = i
                    bestVal = moveVal
                    
        print(moves, self.current_player)
        return bestMove

    
    @classmethod
    def whose_turn(self, board: List[T], values: List[T]):
        if len(board) != 9 or self.was_won(board, values):
            return -1
      
        n1 = board.count(values[1])
        n2 = board.count(values[2])
        
        if n1 == n2 or n1 + 1 == n2:
            return 1
        elif n2 + 1 == n1:
            return 2
        else:
            return -1

    @classmethod
    def is_board_empty(self, board: List[T]):
        for position in board:
            if position != self.values[0]:
                return False
        return True



    @classmethod
    def was_won(self, board: List[T], values: List[T]):
    
        for scenario in self.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                if board[scenario[0]] != values[0]:
                    return True
        
        return False

    @classmethod
    def is_board_complete(self, board: List[T], values: List[T]) -> bool:
        for position in board:
            if position == values[0]:
                return False
        return True

 
    @classmethod
    def evaluate(self, board: List[T], depth):
        for scenario in self.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                if board[scenario[0]] == self.values[self.current_player]:
                    return pow(2, 9 - depth) / (1 if depth == 0 else depth + 1)
                else: 
                    return -pow(2, 9 - depth) / (1 if depth == 0 else depth + 1)
        return 0
    
    @classmethod
    def minimax(self, board: List[T], depth: int, isMaximizingPlayer: bool):
        score = self.evaluate(board, depth)
        # 2 0 1
        # 2 1 2
        # 2 1 2
        
        if(self.was_won(board, self.values)):
            #print(board, self.was_won(board, self.values), int(score), depth)
            return score
    
        elif self.is_board_complete(board, self.values):
            #print(board, self.was_won(board, self.values), 0, depth)
            return 0
        elif isMaximizingPlayer: 
            bestVal = -100000    
            for i in range(0,9) :
                if board[i] == self.values[0]:
                    board[i] = self.values[self.current_player] if isMaximizingPlayer else self.values[1 if self.current_player == 2 else 2]
                    bestVal = max(bestVal, self.minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i] = self.values[0]
                   


        else :    
            bestVal = 100000  
            for i in range(0,9) :
                if board[i] == self.values[0]:
                    board[i] = self.values[self.current_player] if isMaximizingPlayer else self.values[1 if self.current_player == 2 else 2]
                    bestVal = min(bestVal, self.minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i] = self.values[0]            
                     
        return bestVal
