import sys
import collections

def parse_input(filename):
    list1 = []
    list2 = []

    with open('../../puzzles/01/' + filename, encoding="utf-8") as f:
        for line in f:
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))

    return list1, list2

def total_distance():
    list1.sort()
    list2.sort()

    length = len(list1)
    total = 0

    for i in range(length):
        total += abs(list1[i] - list2[i])

    return total

def similarity_score():
    list2_frequencies = collections.Counter(list2)
    score = 0

    for n in list1:
        score += n * list2_frequencies[n]

    return score

filename = sys.argv[1]
list1, list2 = parse_input(filename)

print(total_distance())
print(similarity_score())