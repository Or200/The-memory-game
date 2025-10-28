from .my_io import input_nums

def create_board() -> list[list]:
    size = input_nums()
    x = size[0]
    y = size[1]
    matrix = []
    for i in range(y):
        sub_matrix = []
        for j in range(x):
            sub_matrix.append("X")
        matrix.append(sub_matrix)
    return matrix

    

