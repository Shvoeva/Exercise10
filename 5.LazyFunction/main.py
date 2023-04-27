def get_value(n: int):

    for x in range(n + 1):
        if x == 0:
            yield -10
        elif x % 3:
            yield 45
        elif x % 5:
            yield (x / 5) + 93
        else:
            yield x / 2

if __name__ == '__main__':

    assert list(get_value(3)) == [-10, 45, 45, 93.6]
    assert list(get_value(7)) == [-10, 45, 45, 93.6, 45, 45, 94.2, 45]