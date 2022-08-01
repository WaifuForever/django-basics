from typing import List
from random import randint
from src.application.domain.models import GameModel

class MoveService:
    # win scenarios
    scenarios = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    values = []
    currentPlayer = -1


    @classmethod
    async def best_move(self, request):
        game = GameModel(**request.json)
        bestVal = -1000
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

        self.currentPlayer = {
                -1: -1,
                1: self.values[1],
                2: self.values[2]

            }[self.whoseTurn(game.board)]

        if self.currentPlayer == -1:
            return -1          
            

        for i in range(0,9) :
            #print("%d == %d - %r" % (game.board[i], game.values[0], game.board[i] == game.values[0]))
            if game.board[i] == self.values[0]:
                game.board[i] = self.currentPlayer
                
                moveVal = self.minimax(game.board, 0, False)
                moves.append((i, moveVal))
                game.board[i] = self.values[0]
                if moveVal > bestVal:
                    bestMove = i
                    bestVal = moveVal
                    
        print(moves)
        return bestMove

    @classmethod
    def whoseTurn(self, board: List[int]):
        if len(board) != 9:
            return -1
      
        n1 = board.count(self.values[1])
        n2 = board.count(self.values[2])
        
        if n1 == n2 or n1 + 1 == n2:
            return 1
        elif n2 + 1 == n1:
            return 2
        else:
            return -1

    @classmethod
    def is_board_empty(self, board: List[int]):
        for position in board:
            if position != self.values[0]:
                return False
        return True

    @classmethod
    def was_won(self, board: List[int]):
    
        for scenario in self.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                if board[scenario[0]] != self.values[0]:
                    return True
        
        return False

    @classmethod
    def is_board_complete(self, board: List[int]) -> bool:
        for position in board:
            if position == self.values[0]:
                return False
        return True

    @classmethod
    def evaluate(self, board: List[int]):
        for scenario in self.scenarios:
            if board[scenario[0]] == board[scenario[1]] and board[scenario[1]] == board[scenario[2]]:
                if board[scenario[0]] == self.currentPlayer:
                    return 10
                else: 
                    return -10
        return 0
    
    @classmethod
    def minimax(self, board: List[int], depth: int, isMaximizingPlayer: bool):
        score = self.evaluate(board)
       
        #print(board, self.was_won(board, self.values), score)
        if(self.was_won(board)):
            print(board)
            return score
    
        elif self.is_board_complete(board):
            return 0
        elif isMaximizingPlayer:
            best = -10000          
            for i in range(0,9) :
                if board[i] == self.values[0]:
                    board[i] = self.values[1] if isMaximizingPlayer else self.values[2]
                    best = max(best, score + self.minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i] = self.values[0]
                   
            print(best, depth)
            return best


        else :
            best = 10000        
            for i in range(0,9) :
                if board[i] == self.values[0]:
                    board[i] = self.values[2]
                    best = min(best, score + self.minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i] = self.values[0]            
                     
            print(best, depth)
            return best
