import numpy as np

DATA_PATH = "inputs/day09.txt"


def load_data(DATA_PATH):
    with open(DATA_PATH) as file:
        input = np.loadtxt(DATA_PATH, dtype=str)
    data = np.array([[int(digit) for digit in line] for line in input])
    return data


def get_min(data):
    # Returns boolean with minimums
    assert len(set([len(row) for row in data])) == 1, "Invalid Data"
    rows = len(data)
    cols = list(set([len(row) for row in data]))[0]
    print(f"Num. Rows: {rows}")
    print(f"Num. Cols: {cols}")
    output = np.zeros([rows, cols]).astype(int)

    # Brute force
    for i in range(rows):
        for j in range(cols):
            if i == 0:
                left = 10
            else:
                left = data[i - 1, j]
            try:
                right = data[i + 1, j]
            except Exception as e:
                right = 10

            if j == 0:
                top = 10
            else:
                top = data[i, j - 1]
            try:
                bottom = data[i, j + 1]
            except Exception as e:
                bottom = 10

            if data[i, j] < min(left, right, top, bottom):
                output[i, j] = 1

    return output


def get_risk(data):
    mins = get_min(data)
    rows = len(data)
    cols = list(set([len(row) for row in data]))[0]

    risk = 0

    # Brute force
    for i in range(rows):
        for j in range(cols):
            if mins[i, j] == 1:
                risk += data[i, j] + 1

    return risk


def get_min_indices(data):
    mins = get_min(data)
    return [point for point in zip(*np.where(mins == 1))]


# def get_basin(data, start_point: tuple):
#     """Return Matrix of zeros and ones corresponding to whether or not a
#     point is part of a basin starting at a given min.

#     Args:
#         data ([type]): [description]
#         start_point (tuple): [description]
#     """

#     x, y = start_point


def basin_indices(point, data, indices=None):
    """Recursive function to get indices for a basin starting at a given point.

    Args:
        point ([type]): [description]
        data ([type]): [description]
        indices ([type], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    if indices is None:
        indices = [point]
    x, y = point
    # left
    left = (x - 1, y)
    if left in indices:
        pass
    elif x == 0:
        pass
    elif data[x - 1, y] != 9:
        indices.append(left)
        indices = basin_indices(left, data, indices)
    # right
    right = (x + 1, y)
    if right in indices:
        pass
    else:
        try:
            right_d = data[x + 1, y]
        except Exception as e:
            pass
        else:
            if right_d != 9:
                indices.append(right)
                indices = basin_indices(right, data, indices)
    # top
    top = (x, y - 1)
    if top in indices:
        pass
    elif y == 0:
        pass
    elif data[x, y - 1] != 9:
        indices.append(top)
        indices = basin_indices(top, data, indices)
    # bottom
    bottom = (x, y + 1)
    if bottom in indices:
        pass
    else:
        try:
            bottom_d = data[x, y + 1]
        except Exception as e:
            pass
        else:
            if bottom_d != 9:
                indices.append(bottom)
                indices = basin_indices(bottom, data, indices)

    return list(set(indices))


def get_all_basins(mins, data):
    basins = []
    for min in mins:
        basins.append(basin_indices(min, data))

    print(f"Number of minima: {len(mins)}")
    # basin_set = set(basins)
    print(f"First basin: {basins[0]}")
    basin_sets = [tuple(set(basin)) for basin in basins]
    basin_sets_2 = set(basin_sets)
    output = [list(basin) for basin in basin_sets_2]
    print(f"Number of basins: {len(output)}")
    basin_points = len([point for basin in output for point in basin])
    nine_points = len(np.where(data == 9)[0])
    print(f"Basin points: {basin_points}")
    print(f"9 points: {nine_points}")
    print(f"Calculated points: {basin_points + nine_points}")
    print(f"Total Points: {data.shape[0] * data.shape[1]}")
    return output


# def test_array():

#     return np.array(
#         [1, 1, 0, 1, 0],
#         [
#             0,
#             1,
#         ],
#     )


def main():

    data = load_data(DATA_PATH)
    print(data[0:2])
    mins = get_min(data)
    print(mins[0:2])

    risk = get_risk(data)

    print(f"Risk: {risk}")
    mins = get_min_indices(data)
    print(f"Min indices: {mins}")
    test_basin = basin_indices(mins[1], data, [mins[1]])
    print(f"test basin: {test_basin}\ntest basin area: {len(test_basin)}")
    basins = get_all_basins(mins, data)

    areas = [len(basin) for basin in basins]
    print(f"Basin areas: {areas[0:10]}")
    areas.sort(reverse=True)
    print(f"Basin areas sorted: {areas[0:10]}")

    top_3 = areas[0:3]
    top_3_prod = np.prod(top_3)
    print(f"Product of top 3: {top_3_prod}")


if __name__ == "__main__":
    main()
