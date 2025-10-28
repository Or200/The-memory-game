from time import sleep
from .game import is_frame


def input_nums() -> tuple[int, int]:
    while True:
        try:
            print("size board")
            y_num = int(input("Please write the !! height !! number: "))
            x_num = int(input("Please write the !! width !! number: "))
            if x_num < 10 and y_num < 10 and (x_num * y_num) % 2 == 0:
                return y_num, x_num
            print("Must have one digit, and the product must be even. and num need > 1")
        except:
            print("Must have one digit, and the product must be even. and num need > 1")

def input_choice(cord: tuple[int, int]) -> tuple[int, int]:
    flag_y = True
    flag_x = True

    while flag_y:
        try:
            y_num = int(input("write your choice !! height !! number: "))
            if is_frame(cord[0], y_num):
                flag_y = False
            else:
                print("Error y cord")
        except:
            print("Must have one digit, and the product must be even. and num need > 1")

    while flag_x:
        try:
            x_num = int(input("write your choice !! width !! number: "))
            if is_frame(cord[1], x_num):
                flag_x = False
                return y_num, x_num
            else:
                print("Error x cord")
        except:
            print("Must have one digit, and the product must be even. and num need > 1")

def pause() -> None:
    sleep(5)

def print_board():
    pass

def print_result():
    pass

def log_game():
    pass
