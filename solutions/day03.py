import csv
from collections import Counter


def read_file(path="inputs/day03.txt"):
    output = []
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            output.append(*row)
    return output


def get_number_from_binary(number):
    return int(number, 2)


def gamma_epsilon(data):
    assert len(set([len(row) for row in data])) == 1, "Invalid Data"
    nbits = len(data[0])
    print(f"Binary Length: {nbits}")

    gamma_bits = ""
    epsilon_bits = ""

    for i in range(nbits):
        counter = Counter([row[i] for row in data])
        common = counter.most_common(1)
        digit = common[0][0]
        gamma_bits += digit
        epsilon_bits += "1" if digit == "0" else "0"

    print(gamma_bits)
    print(epsilon_bits)

    return get_number_from_binary(gamma_bits), get_number_from_binary(epsilon_bits)


def get_most_common(data, bit):
    # For oxygen scrubber
    nums = [row[bit] for row in data]
    counter = Counter(nums)
    counts = counter.most_common()
    # If counts are equal return 1
    if counts[0][1] == counts[1][1]:
        return "1"
    else:
        return counts[0][0]


def get_least_common(data, bit):
    # For CO2 Scrubber
    return "1" if get_most_common(data, bit) == "0" else "0"


def filter_data(data, type="most"):
    # Filter data for oxygen or co2. For Oxygen, type='most', for CO2, type='least'
    digits = len(data[0])
    data_f = data.copy()
    print(f"Begin filtering, {len(data)} Rows initial")
    for i in range(digits):
        init_len = len(data_f)
        if type == "most":
            common_digit = get_most_common(data_f, i)
        else:
            common_digit = get_least_common(data_f, i)
        data_f = [row for row in data_f if row[i] == common_digit]
        print(
            f"Filtered digit {i}, {type} common digit: {common_digit}, {len(data_f)} rows remain {round(len(data_f)/init_len * 100)}%"
            # Percentage should be >= 50 for most, <= 50 for least
        )
        if len(data_f) == 1:
            break

    return data_f[0]


def main():
    data = read_file()
    gamma, epsilon = gamma_epsilon(data)
    print(f"G: {gamma} E: {epsilon}\nAnswer: {gamma * epsilon}")
    ox_str = filter_data(data)
    ox_int = get_number_from_binary(ox_str)
    co2_str = filter_data(data, "least")
    co2_int = get_number_from_binary(co2_str)
    print(f"O2 Binary: {ox_str}")
    print(f"O2 int: {ox_int}")
    print(f"CO2 Binary: {co2_str}\nCO2 int: {co2_int}")
    print(f"Life support rating: {ox_int * co2_int}")


if __name__ == "__main__":
    main()
