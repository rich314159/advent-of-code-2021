import numpy as np
import csv


def read_data():
    path = "inputs/day04.txt"
    drawings = []
    boards = []

    with open(path) as f:
        reader = csv.reader(f)
        i = 0
        board_id = -1
        for row in reader:
            if i == 0:
                drawings = [int(d) for d in row]
            else:
                if row == []:
                    board_id += 1
                    boards.append([])
                else:
                    data = row[0].strip().split()
                    # print(data)
                    boards[board_id].append([int(d) for d in data])
            i += 1

    boards_np = [np.array(board) for board in boards]

    return drawings, boards_np


class Board:
    def __init__(self, board_numbers, board_id=None):
        self.numbers = board_numbers
        self.board_id = board_id
        assert len(set(self.numbers.shape)) == 1, "Bingo board needs to be square"
        self._score_history = []
        self.scores = np.zeros(self.numbers.shape, dtype=bool)
        self.bingo = False

    def score(self, number):
        self._score_history.append(number)
        _score_to_add = self.numbers == number
        if (_score_to_add).any():
            # print(
            #     f"Score! Number: {number} Board: {self.board_id if self.board_id else 'unnamed'}"
            # )
            self.scores = self.scores | (_score_to_add)
        self._check_for_bingo(number)

    def _check_for_bingo(self, number):
        for i in range(self.numbers.shape[0]):
            if self.scores[i, :].all() | self.scores[:, i].all():
                self.bingo = True
                if self.scores[i, :].all():
                    self.winning_numbers = self.numbers[i, :]
                else:
                    self.winning_numbers = self.numbers[:, i]
                self.sum_unmarked = np.sum(self.numbers[~self.scores])
                self.number_called = number
                self.final_score = self.sum_unmarked * self.number_called
                # print(
                #     f"BINGO! Drawing: {number} Board:{self.board_id if self.board_id else 'unnamed'} Final Score: {self.final_score}"
                # )
                break

    def score_array(self, numbers):
        for number in numbers:
            self.score(number)


def test_main():
    test_nums = np.array(
        [
            [38, 47, 7, 20, 35],
            [45, 76, 63, 96, 24],
            [98, 53, 2, 87, 80],
            [83, 86, 92, 48, 1],
            [73, 60, 26, 94, 6],
        ]
    )
    print(test_nums)
    test_board = Board(test_nums, "test")
    print(test_board.numbers)
    print(test_board.scores)
    test_draws = [38, 47, 7, 20, 35]
    test_board.score_array(test_draws)
    print(test_board.bingo)


def main():
    drawings, numbers = read_data()
    print(drawings)
    print(numbers[5])
    boards = []
    for id in range(len(numbers)):
        boards.append(Board(numbers[id], str(id)))

    for drawing in drawings:
        for board in boards:
            board.score(drawing)
            if board.bingo:
                winning_board = board
                winning_numbers = board.winning_numbers
                winning_score = board.final_score
                break
        if any([board.bingo for board in boards]):
            break

    print(f"Bingo on board {winning_board.board_id} with final score {winning_score}")

    # ---------------------------------- Part 2 ---------------------------------- #
    for drawing in drawings:
        for board in [board for board in boards if board.bingo == False]:
            board.score(drawing)
            if board.bingo:
                last_winning_board = board
                last_winning_numbers = board.winning_numbers
                last_winning_score = board.final_score
        if all([board.bingo for board in boards]):
            break

    print(
        f"Last winning board {last_winning_board.board_id} with final score {last_winning_score}"
    )


if __name__ == "__main__":
    main()
