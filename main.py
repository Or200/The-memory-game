from memory_game.my_io import input_nums, input_choice
from memory_game.game import create_game_board

def play():
    size = input_nums()
    create_game_board(size)
    input_choice(size)



if __name__ == "__main__":
    play()

