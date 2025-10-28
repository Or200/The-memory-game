from random import sample
from .my_io import input_nums

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
    print(board)
    return board


