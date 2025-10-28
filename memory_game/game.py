from random import sample


def create_clear_board(cord: tuple[int, int]) -> list[list]:
    board = []
    for height in range(cord[0]):
        sub_board = []
        for whidh in range(cord[1]):
            sub_board.append("X")
        board.append(sub_board)
    return board

def create_game_board(cord: tuple[int, int]) -> list[list]:
    n = cord[0] * cord[1]
    chars = "abcdefghijklmnopqrstuvwyz1234567890"
    cards = sample(chars, int(n / 2))
    cards.extend(cards)
    cards = sample(cards, n)
    board = []
    for height in range(cord[0]):
        sub_board = []
        for whidh in range(cord[1]):
            sub_board.append(cards.pop())
        board.append(sub_board)
    return board

def is_finish(work_board: list[list]) -> bool:
    count = 0
    for i in work_board:
        x = 0
        x += i.count('X')
        count += x
    return count == 0

def is_same(work_board: list[list], cord1: tuple[int, int], cord2: tuple[int, int]) -> bool:
    result = work_board[cord1[0] - 1][cord1[1] - 1] == work_board[cord2[0] - 1][cord2[1] - 1]
    return result

def is_frame(cord: int, chr: int) -> bool:
    return cord >= chr
    
def is_was(cord1: tuple[int, int], cord2: tuple[int, int], cords: set) -> bool:
    temp_set = set()
    temp_set.add(cord1)
    temp_set.add(cord2)
    cord = temp_set
    if cord in cords:
        print(f"Error cord: {cord} it's was")
        return True
    else:
        cords.add(str(cord))
        return False
    

