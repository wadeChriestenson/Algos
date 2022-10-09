from time import sleep
import numpy


# Find out how many numbers in a list that are divisible by 'n' number
def divide_by_two(lst, num):
    print('List: ', lst)  # print the list
    print('Numbers in List that can be divided by ' + num)  # print 'n' number
    for x in lst:  # create a for loop to loop through each number in the list
        if x % int(num) == 0:  # if statement to find the moduls of x and 'n' equal zero
            print(x)  # print x
            sleep(.5)
    return


random_num = input('Enter the number you want to find the dividend of.\n')  # ask user for 'n' number
lst_of_nums = numpy.random.randint(0, size=20, high=100)  # create a random list of numbers to search
# lst_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

divide_by_two(lst_of_nums, random_num)  # call function
