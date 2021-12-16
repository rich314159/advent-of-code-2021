import numpy as np


def spl(word):
    return [char for char in word]


def check_subset(super, sub):
    return set(spl(super) + spl(sub)) == set(spl(super))


def number_in_common(a, b):
    return len(set(spl(a)).intersection(set(spl(b))))


def sort_str(st):
    return "".join(sorted(st))


def read_data():
    with open("inputs/day08.txt") as f:
        data = np.loadtxt(f, dtype=str, delimiter=" | ")

    output = [[row[0].split(), row[1].split()] for row in data]

    output_sorted = [[[sort_str(d) for d in col] for col in row] for row in output]
    return output_sorted


def get_segments(row: list) -> dict:
    assert len(row) == 10
    numbers = {}
    # row_sorted = [sort_str(entry) for entry in row]
    for seq in row:
        # Get the unique ones first
        length = len(seq)
        if length == 2:
            numbers[1] = seq
        elif length == 4:
            numbers[4] = seq
        elif length == 3:
            numbers[7] = seq
        elif length == 7:
            numbers[8] = seq
    for seq in row:
        length = len(seq)
        if length == 6:
            # 0, 6, 9
            # if all segments from 4 are in string, then it's 9
            if check_subset(seq, numbers[4]):
                numbers[9] = seq
            elif check_subset(seq, numbers[1]):
                numbers[0] = seq
            else:
                numbers[6] = seq
        elif length == 5:
            # 2, 3, 5
            if check_subset(seq, numbers[1]):
                numbers[3] = seq
            elif number_in_common(seq, numbers[4]) == 2:
                numbers[2] = seq
            else:
                numbers[5] = seq

    numbers_reversed = {v: k for k, v in numbers.items()}
    return numbers_reversed


def map_data(data):
    # for row in data:
    #     numbers = get_segments(row[0])
    #     output = [numbers[d] for d in row[1]]

    return [[get_segments(row[0])[d] for d in row[1]] for row in data]


def main():
    data = read_data()
    # print(data[0:5])

    # print(get_segments(data[0][0]))

    # print(map_data(data[0:5]))
    solution = map_data(data)
    print("Part 1:")
    part1soln = sum([sum([d in [1, 4, 7, 8] for d in row]) for row in solution])
    print(part1soln)
    print("Part 2:")
    part2soln = sum([int("".join([str(d) for d in row])) for row in solution])
    print(part2soln)


if __name__ == "__main__":
    main()
