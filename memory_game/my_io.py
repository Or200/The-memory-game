from time import sleep

def input_nums() -> tuple[int, int]:
    while True:
        try:
            y_num = int(input("Please write the !! height !! number: "))
            x_num = int(input("Please write the !! width !! number: "))
            if x_num < 10 and y_num < 10 and (x_num * y_num) % 2 == 0:
                return y_num, x_num
            print("Must have one digit, and the product must be even. and num need > 1")
        except:
            print("Must have one digit, and the product must be even. and num need > 1")

def input_choice(cord: tuple[int, int]) -> tuple[int, int]:
    y = 0
    x = 0
    print(cord)
    while True:
        try:
            if not y:
                y_num = int(input("write your choice !! height !! number: "))
                if y_num <= cord[0]:
                    y = y_num
                else:
                    print("Error y cord") 
            x_num = int(input("write your choice !! width !! number: "))
            if x_num <= cord[1]:
                x = x_num
                if y and x:
                    return y, x
            else:
                print("Error x cord")  
        except:
            print("Must have one digit, and the product must be even. and num need > 1")



def pause() -> None:
    sleep(5)