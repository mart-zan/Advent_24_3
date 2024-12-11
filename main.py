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

    # Regular expression to extract two nubers
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, instructions)


