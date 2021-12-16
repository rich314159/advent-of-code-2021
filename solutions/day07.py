from collections import Counter
import numpy as np


def read_data():
    with open("inputs/day07.txt") as f:
        data = np.loadtxt(f, delimiter=",", dtype=int)

    return data


DATA = read_data()


def get_distance(counts, point):

    distance = sum([abs(k - point) * v for k, v in counts.items()])

    return distance


def get_distance_2(counts, point):

    distance = sum([sum(range(abs(k - point) + 1)) * v for k, v in counts.items()])

    return distance


def brute(data):
    xmin = min(data)
    xmax = max(data)
    loss = {}
    counts = Counter(DATA)
    for x in range(xmin, xmax + 1):
        loss[x] = get_distance(counts, x)

    min_start = min(loss, key=loss.get)

    return min_start, loss[min_start]


def brute_2(data):
    xmin = min(data)
    xmax = max(data)
    loss = {}
    counts = Counter(DATA)
    for x in range(xmin, xmax + 1):
        loss[x] = get_distance_2(counts, x)

    min_start = min(loss, key=loss.get)

    return min_start, loss[min_start]


def main():
    data = read_data()
    x0 = int(np.median(DATA))
    root, fuel = brute(data)
    print(root)
    print(fuel)
    root_2, fuel_2 = brute_2(data)
    print(root_2)
    print(fuel_2)


if __name__ == "__main__":
    main()
