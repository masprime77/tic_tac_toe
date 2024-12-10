import os
import time

game_end = False
next_character = "X"

def print_board():
    for i in range(3):
        print("+-----+-----+-----+\n" +
              "|  {}  |  {}  |  {}  |".format(characters[i][0], characters[i][1], characters[i][2]))

    print("+-----+-----+-----+")

def clear_board():
    os.system("clear")

    for i in range(3):
        for j in range(3):
            characters[i][j] = " "

characters = [["1", "2", "3"],
              ["4", "5", "6"],
              ["7", "8", "9"],]

print_board()

print("\n" + "Seleccionar un número de casilla 'X' comienza.")

time.sleep(5)

clear_board()
print("Empiezan las X's")

while not game_end:
    next_move = input("Siguiente jugada: ")
    if next_move == "1":
        characters[0][0] = next_character
    elif next_move == "2":
        characters[0][1] = next_character
    elif next_move == "3":
        characters[0][2] = next_character
    elif next_move == "4":
        characters[1][0] = next_character
    elif next_move == "5":
        characters[1][1] = next_character
    elif next_move == "6":
        characters[1][2] = next_character
    elif next_move == "7":
        characters[2][0] = next_character
    elif next_move == "8":
        characters[2][1] = next_character
    elif next_move == "9":
        characters[2][2] = next_character
    else:
        next_character

print_board()
