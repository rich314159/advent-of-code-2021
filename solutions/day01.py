import numpy as np

DATA_PATH = "inputs/day01.txt"


def load_data(DATA_PATH):
    with open(DATA_PATH) as file:
        input = np.loadtxt(DATA_PATH, dtype=int)
    data = input
    return data


def get_increases(data):
    increases = []
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            increases.append(1)
        else:
            increases.append(0)

    return increases


def get_3_increases(data):
    data_3s = [sum(data[i : i + 3]) for i in range(len(data) - 2)]
    print(f"Data first 3: {data[0:3]}\nData first 3 sums: {data_3s[0:3]}")
    increases = []
    for i in range(1, len(data_3s)):
        if data_3s[i] > data_3s[i - 1]:
            increases.append(1)
        else:
            increases.append(0)

    return increases


def main():
    data = load_data(DATA_PATH)
    print(data)
    increases = get_increases(data)
    # print(f"increases: {increases}")
    print(f"# of increases: {sum(increases)}")
    increases3 = get_3_increases(data)
    # print(f"increases: {increases}")
    print(f"# of increases: {sum(increases3)}")


if __name__ == "__main__":
    main()
