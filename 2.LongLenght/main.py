def get_long(words: list):

    return list(map(lambda x: len(x), words))

if __name__ == '__main__':
    
    assert get_long(['Tina', 'Raj', 'Tom']) == [4, 3, 3]