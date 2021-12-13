import numpy as np
from collections import Counter

MAX_AGE = 6
NEW_AGE = 8


def read_data():
    path = "inputs/day06.txt"

    with open(path) as f:
        data = np.loadtxt(f, dtype=int, delimiter=",")

    return data


def get_counts(data):
    counter = Counter(data)

    # print(counter)
    counts = [counter[i] if counter[i] else 0 for i in range(NEW_AGE + 1)]
    print(counts)
    return counts


def increment_time(data):
    output = []

    new_fish_count = 0
    for fish in data:
        if fish == 0:
            new_fish_count += 1
            output.append(MAX_AGE)
        else:
            output.append(fish - 1)
    output.extend([NEW_AGE] * new_fish_count)

    return output


def increment_counts(counts):
    assert len(counts) == NEW_AGE + 1
    new_counts = [0] * (NEW_AGE + 1)
    for i in range(len(counts)):
        if i == 0:
            new_counts[NEW_AGE] += counts[i]
            new_counts[MAX_AGE] += counts[i]
        else:
            new_counts[i - 1] += counts[i]

    return new_counts


def main():
    data = read_data()
    counts = get_counts(data)
    counts1 = counts.copy()
    counts2 = counts.copy()
    data1 = data.copy()
    data2 = data.copy()
    NUM_DAYS_1 = 80

    for day in range(NUM_DAYS_1):
        data1 = increment_time(data1)
        counts1 = increment_counts(counts1)

    print(f"Fish count: {len(data1)}\nCheck counts: {sum(counts1)}")
    NUM_DAYS_2 = 256

    for day in range(NUM_DAYS_2):
        counts2 = increment_counts(counts2)

    print(f"Fish count: {sum(counts2)}")


if __name__ == "__main__":
    main()
