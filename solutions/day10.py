import numpy as np

MATCH = {"(": ")", "[": "]", "<": ">", "{": "}"}
OPEN = ["(", "[", "<", "{"]
CLOSE = [")", "]", ">", "}"]
SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORE2 = {")": 1, "]": 2, "}": 3, ">": 4}


def read_data():
    with open("inputs/day10.txt") as f:
        data = np.loadtxt(f, dtype=str)

    return data


def invalid_found(row):
    track = []
    for ch in row:
        if ch in OPEN:
            track.append(ch)
        elif ch in CLOSE:
            if MATCH[track[-1]] == ch:
                track.pop()
            else:
                return ch
        else:
            raise ValueError("invalid character")
    return None


def get_match_score(row):
    track = []
    for ch in row:
        if ch in OPEN:
            track.append(ch)
        elif ch in CLOSE:
            if MATCH[track[-1]] == ch:
                track.pop()
            else:
                raise ValueError("invalid character")

        else:
            raise ValueError("invalid character")
    track.reverse()
    matches = [MATCH[ch] for ch in track]

    score = 0

    for match in matches:
        score = score * 5 + SCORE2[match]
        # print(score)

    return score


def main():
    # print(read_data()[0])

    # print(invalid_found("((([)))"))
    # print(invalid_found("((([])))"))

    data = read_data()
    invalids = [invalid_found(row) for row in data]
    # print(invalids[0:50])
    valids = [d for d, i in zip(data, invalids) if not i]
    # print(valids[0:5])
    # print([SCORE[d] if d else 0 for d in invalids[0:50]])

    # print(sum([SCORE[d] if d else 0 for d in invalids]))
    # print(data[1])
    # print(get_matches(data[1]))
    # test = get_matches(data[1])
    # print([SCORE2[d] for d in test])
    print(f"Match score: {get_match_score(valids[0])}")
    # print(valids[0])
    scores = [get_match_score(d) for d in valids]

    scores.sort()

    # print(scores)

    middle_score = scores[int((len(scores) - 1) / 2)]
    print(f"Middle Score: {middle_score}")


if __name__ == "__main__":
    main()
