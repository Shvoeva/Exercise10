def exponentiate(X :list, Y :list):

    assert len(X) == len(Y)

    exponent = map(lambda x: pow(*x), zip(X, Y))
    return list(exponent)

if __name__ == '__main__':

    X = [2, 3, 4]
    Y = [10, 11, 12]
    assert exponentiate(X, Y) == [1024, 177147, 16777216]
