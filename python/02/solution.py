from collections import defaultdict


def parse_input(filename):
    reports = []

    with open("../../puzzles/02/" + filename, encoding="utf-8") as f:
        for line in f:
            reports.append([int(level) for level in line.split()])

    return reports


def is_safe(report):
    if report[1] == report[0]:
        return False

    if report[1] > report[0]:
        for i in range(1, len(report)):
            if not (0 < report[i] - report[i - 1] <= 3):
                return False
    elif report[1] < report[0]:
        for i in range(1, len(report)):
            if not (0 < report[i - 1] - report[i] <= 3):
                return False

    return True


def find_total_safe(reports):
    return len([True for report in reports if is_safe(report)])


def convert_report_to_distance_logs(report):
    return [report[i] - report[i - 1] for i in range(1, len(report))]


def is_safe_2(distance_log):
    if distance_log[0] == 0:
        return False

    increasing = distance_log[0] > 0

    if increasing:
        for d in distance_log:
            if d <= 0 or d > 3:
                return False
    else:
        for d in distance_log:
            if d >= 0 or d < -3:
                return False

    return True


def is_safe_pair(level1, level2):
    return level1 != level2 and abs(level1 - level2) <= 3


def is_safe_dampened(report):
    length = len(report)

    increasing = all([report[i] < report[i + 1] for i in range(length - 1)])
    if increasing:
        if report[0] - report[1] <= -4:
            return is_safe(report[1:])
        elif report[length - 2] - report[length - 1] <= -4:
            return is_safe(report[: length - 1])
        else:
            return all([report[i] - report[i + 1] > -4 for i in range(1, length - 2)])

    decreasing = all([report[i] > report[i + 1] for i in range(length - 1)])
    if decreasing:
        if report[0] - report[1] >= 4:
            return is_safe(report[1:])
        elif report[length - 2] - report[length - 1] >= 4:
            return is_safe(report[: length - 1])
        else:
            return all([report[i] - report[i + 1] < 4 for i in range(1, length - 2)])

    if report[0] == report[1]:
        return is_safe(report[1:])
    if report[length - 2] == report[length - 1]:
        return is_safe(report[: length - 1])

    for i in range(len(report) - 2):
        if report[i] == report[i + 1]:
            return is_safe(report[:i] + report[i + 1 :]) or is_safe(
                report[: i + 1] + report[i + 2 :]
            )


def find_total_safe_2(distance_logs):
    total = 0
    for log in distance_logs:
        if is_safe_2(log):
            total += 1
    return total


def find_total_safe_dampened(reports, distance_logs):
    total = 0
    for i, log in enumerate(distance_logs):
        if is_safe_dampened(log):
            total += 1
        else:
            print(reports[i], " ", log)
    return total


# reports = parse_input("input.txt")
# print(find_total_safe(reports))

reports = parse_input("input.txt")
print(find_total_safe_dampened(reports))
