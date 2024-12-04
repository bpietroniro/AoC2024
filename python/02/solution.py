def parse_input(filename):
    reports = []

    with open("../../puzzles/02/" + filename, encoding="utf-8") as f:
        for line in f:
            reports.append([int(level) for level in line.split()])

    return reports


# Part 1
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


# Alternative approach to Part 1
def convert_reports_to_distance_logs(report):
    distance_logs = []
    for report in reports:
        distance_logs.append([report[i] - report[i - 1] for i in range(1, len(report))])

    return distance_logs


def is_safe_by_distance_log(log):
    if log[0] == 0:
        return False

    increasing = log[0] > 0

    if increasing:
        for d in log:
            if d <= 0 or d > 3:
                return False
    else:
        for d in log:
            if d >= 0 or d < -3:
                return False

    return True


def find_total_safe_by_distance_logs(logs):
    total = 0
    for log in logs:
        if is_safe_by_distance_log(log):
            total += 1
    return total


# Part 2
def is_safe_dampened(report):
    length = len(report)
    if is_safe(report) or is_safe(report[1:]) or is_safe(report[: length - 1]):
        return True

    for i in range(1, length - 1):
        if is_safe(report[:i] + report[i + 1 :]):
            return True

    return False


def find_total_safe_dampened(reports):
    return len([True for report in reports if is_safe_dampened(report)])


reports = parse_input("input.txt")
print(find_total_safe(reports))
print(find_total_safe_by_distance_logs(convert_reports_to_distance_logs(reports)))
print(find_total_safe_dampened(reports))
