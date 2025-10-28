from memory_game.my_io import input_nums, input_choice
from memory_game.game import create_game_board, create_clear_board, is_same, is_was, is_finish

def play():
    my_cords = set()
    size = input_nums()
    view = create_clear_board(size)
    work = create_game_board(size)
    while True:
        
        print("card1")
        choice1 = input_choice(size)
        view[choice1[0] - 1][choice1[1] - 1] = work[choice1[0] - 1][choice1[1] - 1]
                 
        while True:
            print("card2")
            choice2 = input_choice(size)
            if choice2 != choice1:
                view[choice2[0] - 1][choice2[1] - 1] = work[choice2[0] - 1][choice2[1] - 1]
                break
            else:
                print("same cards")

        print(view)

        if is_same(work, choice1, choice2):
            print("is same")
        else:
            view[choice1[0] - 1][choice1[1] - 1] = 'X'
            view[choice2[0] - 1][choice2[1] - 1] = 'X'

        if is_finish(view):
            print("You finish")
            break

        
        print(view)

if __name__ == "__main__":
    play()

