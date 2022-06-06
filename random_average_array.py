#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: May 2022
# This is a highest number checker

import random


def highest_number(random_number):
    # this function finds the highest number
    biggest_num = random_number[0]
    # process
    for check in random_number:
        if check > biggest_num:
            biggest_num = check
    return biggest_num


def main():
    # this function gathers the 10 random numbers
    random_number = []
    total = 0
    counter = 0
    rounded = 0
    # this loop gathers the 10 numbers, randomly through 1 to 100
    for counter in range(10):
        random_num = random.randint(0, 100)
        random_number.append(random_num)
        print("The random number is {0}".format(random_num))
    # output
    biggest_num = highest_number(random_number)
    print("\nThe highest number is {0}".format(biggest_num))


if __name__ == "__main__":
    main()
