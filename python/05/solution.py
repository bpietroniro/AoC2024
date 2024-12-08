from collections import defaultdict
from functools import cmp_to_key


def parse_input(filename):
    rules_dict = defaultdict(set)
    updates = []
    with open("../../puzzles/05/" + filename, encoding="utf-8") as f:
        # parse rules
        for line in f:
            if line == "\n":
                break
            first, second = line.strip().split("|")
            rules_dict[int(first)].add(int(second))

        # parse updates
        for line in f:
            updates.append([int(num) for num in line.strip().split(",")])

    return updates, rules_dict


def is_correct(update, rules_dict):
    seen = set()
    for page_num in update:
        seen.add(page_num)
        if not rules_dict[page_num].isdisjoint(seen):
            return False
    return True


def find_middle_page_number(update):
    return update[len(update) // 2]


def fix_incorrect_ordering(update, rules_dict):
    return


# part 1
def calculate_correct(updates, rules_dict):
    middle_page_sum = 0

    for update in updates:
        if is_correct(update, rules_dict):
            middle_page_sum += find_middle_page_number(update)

    return middle_page_sum


# part 2
def calculate_corrected(updates, rules_dict):
    def comparison(a, b):
        if a in rules_dict[b]:
            return 1
        else:
            return -1

    middle_page_sum = 0

    for update in updates:
        if not is_correct(update, rules_dict):
            corrected_update = sorted(update, key=cmp_to_key(comparison))
            middle_page_sum += find_middle_page_number(corrected_update)

    return middle_page_sum


updates, rules_dict = parse_input("input.txt")
# for rule in rules_dict:
#     print(f"{rule}: {rules_dict[rule]}")
# print(calculate_correct(updates, rules_dict))
print(calculate_corrected(updates, rules_dict))
