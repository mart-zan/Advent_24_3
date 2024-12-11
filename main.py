import numpy as np
import re

# Advent of code
# --- Day 2: Red-Nosed Reports ---
def read_instructions(filename: str):

    my_file = open(filename, "r")
    data = my_file.read()
    my_file.close()
    # Returns
    return data



if __name__ == '__main__':
    # Read and close file
    instructions = read_instructions("input.txt")

    # Regular expression to extract two numbers
    pattern = r"mul\((\d+),(\d+)\)"
    numbers_list = re.findall(pattern, instructions)

    sum_mul = 0

    # Inititalization
    for numbers in numbers_list:
        num1, num2 = numbers
        sum_mul += int(num1) * int(num2)

    print("Final sum is " + str(sum_mul))
