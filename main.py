import random

print("Welcome to Tic Tac Toe!")
print("-----------------------")

possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_board = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
rows = 3
columns = 3

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|" , end="")
        for y in range(columns):
            print("" , game_board[x][y], end=" |")
    print("\n+---+---+---+")

printGameBoard()