import numpy as np


def read_data():
    path = "inputs/day05.txt"
    with open(path) as f:
        data = np.loadtxt(f, dtype=str)
    output = []
    for row in data:
        data_row = [row[0].split(","), row[2].split(",")]
        output.append(data_row)

    return np.array(output, dtype=int)


def get_line(row):
    x_min = min(row[0][0], row[1][0])
    x_max = max(row[0][0], row[1][0])
    y_min = min(row[0][1], row[1][1])
    y_max = max(row[0][1], row[1][1])
    x1, y1, x2, y2 = row[0][0], row[0][1], row[1][0], row[1][1]
    if x1 == x2:
        points = np.array([[x1, y] for y in range(y_min, y_max + 1)])
    elif y1 == y2:
        points = np.array([[x, y1] for x in range(x_min, x_max + 1)])
    else:
        if x1 > x2:
            x = range(x1, x2 - 1, -1)
        else:
            x = range(x1, x2 + 1)
        if y1 > y2:
            y = range(y1, y2 - 1, -1)
        else:
            y = range(y1, y2 + 1)
        points = np.array([[x, y] for x, y in zip(x, y)])

    return points


def get_grid(data):
    size = data.max()
    grid = np.zeros((size + 1, size + 1))

    for row in data:
        points = get_line(row)
        if points is not None:
            for point in points:
                grid[point[0], point[1]] += 1

    return grid


def main():
    data = read_data()
    print(data[0:5])
    print(data[0][0])

    print(data.max())

    print(get_line(data[1])[0:5])

    grid = get_grid(data)

    total = (grid >= 2).sum()

    print(f"Number of dangerous areas: {total}")


if __name__ == "__main__":
    main()
