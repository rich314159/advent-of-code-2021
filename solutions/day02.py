import csv

DATA_PATH = "inputs/day02.txt"


def read_file(path):
    output = []
    with open(path) as f:
        reader = csv.reader(f, delimiter=" ")
        for row in reader:
            output.append(row)
    output = [[row[0], int(row[1])] for row in output]
    return output


def get_final_coord(data, start=[0, 0]):
    position = start.copy()
    for row in data:
        if row[0] == "forward":
            position[0] += row[1]
        elif row[0] == "down":
            position[1] += row[1]
        elif row[0] == "up":
            position[1] -= row[1]
        else:
            raise ValueError("Invalid direction!")

    print(f"Final Position: {position}")
    return position[0] * position[1]


def get_final_coord_2(data, start=[0, 0, 0]):
    position = start.copy()

    for row in data:
        if row[0] == "forward":
            position[0] += row[1]
            position[1] += position[2] * row[1]
        elif row[0] == "down":
            position[2] += row[1]
        elif row[0] == "up":
            position[2] -= row[1]
        else:
            raise ValueError("Invalid direction!")

    print(f"Final Position: {position}")
    return position[0] * position[1]


def main():
    data = read_file(DATA_PATH)
    # print(data)
    solution1 = get_final_coord(data)
    print(solution1)
    solution2 = get_final_coord_2(data)
    print(solution2)


if __name__ == "__main__":
    main()
