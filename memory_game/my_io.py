from time import sleep

def input_nums() -> tuple[int, int]:
    while True:
        try:
            x_num = int(input("Please write the !! height !! number: "))
            y_num = int(input("Please write the !! width !! number: "))
            if x_num < 10 and y_num < 10 and (x_num * y_num) % 2 == 0:
                return x_num, y_num
            print("Must have one digit, and the product must be even. and num need > 1")
        except:
            print("Must have one digit, and the product must be even. and num need > 1")

def pause() -> None:
    sleep(5)