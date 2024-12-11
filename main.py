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
    pattern_mul = r"mul\((\d+),(\d+)\)"
    numbers_list = re.findall(pattern_mul, instructions)

    # Initialization
    sum_mul = 0

    ### TASK 1
    for numbers in numbers_list:
        num1, num2 = numbers
        sum_mul += int(num1) * int(num2)

    print("Final sum is " + str(sum_mul))

    ### TASK 2
    # Patterns
    # pattern_do = r"\\do()"
    # pattern_dont = r"\\don't()"

    # Find all instructions do/dont/mul
    all_matches = re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", instructions)

    # Initialization
    mul_enabled = True  # Multiplications start enabled
    sum_mul = 0         # Sum of enabled multiplications

    # Process each instruction in order
    for match in all_matches:
        instruction = match.group()

        if instruction == "do()":  # If do found
            mul_enabled = True  # Enable multiplications
        elif instruction == "don't()":  # If dont found
            mul_enabled = False  # Disable multiplications
        else:  # It's a mul(x, y) instruction
            if mul_enabled:
                # Extract the two numbers
                num1, num2 = map(int, re.findall(r"\d+", instruction))
                sum_mul += num1 * num2

    print("Final sum with do and dont is " + str(sum_mul))

