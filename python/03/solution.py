import re


def parse_input(filename, matcher):
    instructions = []

    with open("../../puzzles/03/" + filename, encoding="utf-8") as f:
        for line in f:
            matches = re.findall(matcher, line)
            instructions += matches

    return instructions


def interpret(instructions):
    enabled = True
    mult_operations = []

    for instruction in instructions:
        if instruction.startswith("don't"):
            enabled = False
        elif instruction.startswith("do"):
            enabled = True
        elif enabled:
            mult_operations.append(instruction)

    return mult_operations


def convert_to_number_pairs(mult_operations):
    return [str(i).strip("mul()").split(",") for i in mult_operations]


def calculate_total(number_pairs):
    return sum([int(pair[0]) * int(pair[1]) for pair in number_pairs])


part_1_matcher = r"mul\(\d{1,3}\,\d{1,3}\)"
part_2_matcher = r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\)"

# Part 1
instructions = parse_input("input.txt", part_1_matcher)
print(calculate_total(convert_to_number_pairs(instructions)))

# Part 2
instructions = parse_input("input.txt", part_2_matcher)
print(calculate_total(convert_to_number_pairs(interpret(instructions))))
