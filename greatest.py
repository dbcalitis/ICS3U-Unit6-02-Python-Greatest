#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program determines the greatest number

import random


def greatest(num_list):
    # This function determines the largest number out of the list.
    for counter in range(len(num_list)):
        if counter == 0:
            greatest_num = num_list[counter]
        else:
            if greatest_num < num_list[counter]:
                greatest_num = num_list[counter]

    return greatest_num


def main():
    # This function is the main function
    number_list = []

    # process & output
    print("Here is a list of random numbers:\n")

    for counter in range(10):
        random_num = random.randint(1, 100)
        number_list.append(random_num)
        print("The random number {0} is: {1}".format(counter + 1, random_num))

    print("\nThe largest number is {0}".format(greatest(number_list)))

    print("\nDone.")


if __name__ == "__main__":
    main()
