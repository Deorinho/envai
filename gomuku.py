#2-player Freestyle Gomuku
#by Abhishek Deorukhkar
BLACK = "b"
WHITE = "w"
EMPTY = "o"
#initiate class gomuku
class Gomuku():

#create the gameboard remember that the tiles are placed on the verticies/intersections of the board - "o" will act as the placeholder for the verticies    
    def __init__(self, size = 16) -> None:
        self.size = size
        self.board = [[EMPTY]* size for b in range(size) ]
        self.currentPlayer = BLACK

    def __repr__(self):
        printed = ""
        for i in range(len(self.board)):
            for v in range(len(self.board[i])):
                if v != len(self.board[i]) - 1:
                    #the hypen is the horizontal line that connects the verticies together
                    printed += self.board[i][v] + "-"
                else:
                    printed += self.board[i][v] + "\n"
            if i != len(self.board) - 1:
                #nested for loops to create the vertical  
                for v in range(len(self.board[i])):
                    if v != len(self.board[i]) - 1:
                        printed += "| "
                    else:
                        printed += "|\n"
        return printed

    def isValid(self, pos):
        return pos < self.size and pos >= 0
#place the tile on a valid vertice for each player
    def placePiece(self, row,col):
        if not self.isValid(row) or not self.isValid(col) or self.board[row][col] != EMPTY:
            print("invalid move!")
            return 0

        self.board[row][col] = self.currentPlayer
        self.currentPlayer = BLACK if self.currentPlayer == WHITE else WHITE
        return 1

if __name__ == "__main__":
    game = Gomuku()
    while 1:
        print(game)
        while 1:
            #surrender and exit after every turn
            print(game.currentPlayer + " TURN")
            ff = input("Surrender? Y/N: ") 
            if ff.lower() == "y":
                print(game.currentPlayer + " Wins")
                exit()
            x = input('Enter row: ')
            y = input('Enter col: ')
            if game.placePiece(int(x), int(y)):
                break

# some things to consider:
#1. when the program starts my surrender prompt is the first thing the user sees after the turn count
#2. Need to add a loop to check for win, the computer should let the user know when the player wins from 5 in a row horizontally, vertrically and diagonally
#3. create a readme with all design choices and my step by step instructions on how I created the app1