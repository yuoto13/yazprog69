def f(matrix) -> int:
    n = min(len(matrix), len(matrix[0]))

    s = 0
    for i in range(n):
        if (x := matrix[i][i]) % 2 == 0:
            s += x
    return s


def main():
    matrix = [
        [3, 1, 1, 1],
        [1, 2, 1, 1],
        [1, 1, 3, 1],
        [1, 1, 1, 4],
        [1, 1, 1, 1],
    ]
    print(f(matrix))


if __name__ == '__main__':
    main() 