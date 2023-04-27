def get_fahrenheit(celsius: list):

    return list(map(lambda x: x*9/5+32, celsius))

if __name__ == '__main__':
    
    assert get_fahrenheit([39.2, 36.5, 37.3, 37.8]) == [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]