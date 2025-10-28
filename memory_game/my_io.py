
def input_nums() -> tuple[int, int]:
    while True:
        try:
            x_num = int(input("Please write the width number: "))
            y_num = int(input("Please write the height number: "))
            if x_num % 2 == 0 and x_num > 1 and y_num % 2 == 0 and y_num > 1:
                return x_num, y_num
            print("the number must be a single digit and a whole number. and need num > 1")
        except:
            print("the number must be a single digit and a whole number. and need num > 1")
