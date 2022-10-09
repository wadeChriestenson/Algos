from time import sleep

import numpy


def divide_by_two(lst, num):
    print(lst)
    for x in lst:
        if x % 2 == 0:
            print(x, 'can be divided by', num)
            sleep(.5)
    return


random_num = numpy.random.randint(1, size=1, high=10)
lst_of_nums = numpy.random.randint(0, size=20, high=100)
# lst_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

divide_by_two(lst_of_nums, random_num)
