from time import sleep
import numpy


# Find out how many numbers in a list that are divisible by 2 number
def divide_by_two(lst):
    print('List: ', lst)  # print the list
    print('Numbers in List that can be divided by 2')  # print number
    new_lst = [x for x in lst if not x % 2]
    print('New List', new_lst)
    return


lst_of_nums = numpy.random.randint(-10000, 24, 10000)  # create a random list of numbers to search
# lst_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

divide_by_two(lst_of_nums)  # call function
