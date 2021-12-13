import numpy as np


def read_data():
    path = "inputs/day04.txt"

    drawings = []
    boards = ["list of numpy arrays"]
    return drawings, boards


class Board:
    def __init__(self, board_numbers):
        self.numbers = board_numbers
        self._score_history = []

    def score(number):
        self._score_history.append(number)


def main():
    test_board = np.array(
        [
            [38, 47, 7, 20, 35],
            [45, 76, 63, 96, 24],
            [98, 53, 2, 87, 80],
            [83, 86, 92, 48, 1],
            [73, 60, 26, 94, 6],
        ]
    )
    print(test_board)


if __name__ == "__main__":
    main()
