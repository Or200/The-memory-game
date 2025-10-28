from memory_game.my_io import input_nums
from memory_game.game import create_game_board

def play():
    size = input_nums()
    create_game_board(size)


if __name__ == "__main__":
    play()

