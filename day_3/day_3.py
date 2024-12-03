#importing regex library to help with pattern recognition
import re

#taking input.txt as a readable file and stripping all white space
with open("input.txt", "r") as file:
    corrupted_memory = file.read().strip()

#defining the patterns
mul_pattern = r"mul\((\d+),(\d+)\)" 
control_pattern = r"(do\(\)|don't\(\))"

#finding iterations of either mul or control accross corrupted memory
mul_matches = re.finditer(mul_pattern, corrupted_memory)
control_matches = re.finditer(control_pattern, corrupted_memory)

#creates a sorted list of mul and control matches, match function records the starting position of the matches
all_matches = sorted(list(mul_matches) + list(control_matches), key = lambda match: match.start())

#variable defining whether to mul or not, and the total of muls
enabled = True
total = 0

#for loop to iterate through matches. if matches are either do or don't they toggle enabled. else, mul is calculated
for match in all_matches:
    instruction = match.group(0)

    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    else:
        if enabled:
            x, y = map(int, match.groups())
            total += x * y

#output total mulls
print("The total of all the mulls is {}.".format(total))

#code for pret toilet - 3467