import numpy as np


def read_data():
    with open("inputs/day12.txt") as f:
        data = np.loadtxt(f, dtype=str)

    output = [tuple(x.split("-")) for x in data]

    return output


def main():
    print(read_data())


if __name__ == "__main__":
    main()
