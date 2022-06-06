#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: May 2022
# This is a array column and row adder

import random


def array_mean(grid, row_number, column_number):
    # this function calculates the mean of all the elements in a array

    sum_array = 0
    for row in grid:
        for array_element in row:
            sum_array += array_element

    sum_array = sum_array / (row_number * column_number)

    return sum_array


def main():
    # this function creates a 2D array

    array = []

    # input
    row = input("Enter in the number of rows: ")
    column = input("Enter in the number of columns: ")
    print("")

    try:
        rows_num = int(row)
        columns_int = int(column)

        if rows_num < 0:
            print("That is an invalid integer.")
        elif columns_int < 0:
            print("That is an invalid integer.")

        else:
            for loop_counter_rows in range(0, rows_num):
                temp_column = []
                for loop_counter_columns in range(0, columns_int):
                    random_number = random.randint(0, 50)
                    temp_column.append(random_number)
                    print("{0} ".format(random_number), end="")
                array.append(temp_column)
                print("")

            rounded_array_mean = round(array_mean(array, rows_num, columns_int), 2)
            print("")
            print("The mean of the matrix is: {0} ".format(rounded_array_mean))

    except Exception:
        print("Invalid Input!")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
