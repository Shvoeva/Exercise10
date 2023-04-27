if __name__ == '__main__':

    sentences = ['капитан джек воробей',
                 'капитан дальнего плавания',
                 'ваша лодка готова, капитан']

    list_cap_count = map(lambda x: x.count('капитан'), sentences)
    cap_count = sum(list_cap_count)

    print(cap_count)
