def zeros(n):
    result = 0
    for i in range(5, n + 1, 5):
        while i % 5 == 0:
            result += 1
            i //= 5
    return result


def main():
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7


if __name__ == '__main__':
    main()
