from memory_game.my_io import input_nums, input_choice, pause, print_board, time_game
from memory_game.game import create_game_board, create_clear_board, is_same, is_was, is_finish
from datetime import datetime

def play():
    start = datetime.now()
    my_cords = set()
    size = input_nums()
    view = create_clear_board(size)
    work = create_game_board(size)
    print_board(view)
    while True:
        
        print("card1")
        choice1 = input_choice(size)
        if is_was(choice1, my_cords):
            print("is was - c1")
        else:
            view[choice1[0] - 1][choice1[1] - 1] = work[choice1[0] - 1][choice1[1] - 1]
            print_board(view)
                 

        while True:
            print("card2")
            choice2 = input_choice(size)
            if is_was(choice2, my_cords):
                print("is was - c2")
            else:
                if choice2 != choice1:
                    view[choice2[0] - 1][choice2[1] - 1] = work[choice2[0] - 1][choice2[1] - 1]
                    break
                else:
                    print("same cards")

        print_board(view)

        if is_same(work, choice1, choice2):
            my_cords.add(choice1)
            my_cords.add(choice2)
            print(my_cords)
        else:
            if is_was(choice1, my_cords):
                print("is was - tre again")
                view[choice2[0] - 1][choice2[1] - 1] = 'X'
            if is_was(choice1, my_cords):
                print("is was - tre again")
                view[choice1[0] - 1][choice1[1] - 1] = 'X'
            else:
                view[choice1[0] - 1][choice1[1] - 1] = 'X'
                view[choice2[0] - 1][choice2[1] - 1] = 'X'



        if is_finish(view):
            finish = datetime.now()
            time_game(start, finish)
            print("You finish")
            break

        pause()
        print_board(view)

if __name__ == "__main__":
    play()

