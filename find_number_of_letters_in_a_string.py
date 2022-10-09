def numbers_of_letters(string):
    alpha = []
    for x in string:
        if x.isalpha():
            alpha.append(x.lower())
    print(len(alpha), 'letters are in the sentence\n', string)
    return


sentence = input('Write a sentence to find out how many characters are letters.\n')

numbers_of_letters(sentence)
