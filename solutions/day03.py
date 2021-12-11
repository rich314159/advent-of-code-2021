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


def main():
    data = read_file()
    gamma, epsilon = gamma_epsilon(data)
    print(f"G: {gamma} E: {epsilon}\nAnswer: {gamma * epsilon}")


if __name__ == "__main__":
    main()
