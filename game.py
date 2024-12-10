import os
import time


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]

        if all(cell != " " for row in board for cell in row):
            return "Draw"

        return None

def print_board(board):
    os.system('clear')
    for row in board:
        print("+---+---+---+")
        print("| ", end="")
        print(" | ".join(row), end="")
        print(" |")

    print("+---+---+---+")

def get_player_input(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row = move // 3
            col = move % 3
            if board[row][col] == " ":
                return row, col
            else:
                print("Occupied cell. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def main():
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    print_board(board)
    time.sleep(5)

    board = [[" " for _ in range(3)] for _ in range(3)] # Generates a double list 3x3 with whitespaces.
    current_player = "X"

    print_board(board)

    while True:
        row, col = get_player_input(current_player, board)
        board[row][col] = current_player
        print_board(board)

        winner = check_winner(board)
        if winner is not None:
            if winner == "Draw":
                print("It's a tie!")
            else:
                print(f"Player {winner} wins!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == '__main__':
    main()
