def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def is_safe(report):
    is_ordered = (
        all(report[i] < report[i + 1] for i in range(len(report) - 1)) or
        all(report[i] > report[i + 1] for i in range(len(report) - 1))
    )
    is_delta_correct = all(
        abs(report[i + 1] - report[i]) in [1, 2, 3] for i in range(len(report) - 1)
    )
    return is_ordered and is_delta_correct

def is_safe_modified(report, tolerance_count=0):
    if tolerance_count > 1:
        return False
    if is_safe(report):
        return True
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe_modified(new_report, tolerance_count + 1):
            return True
    return False

if __name__ == '__main__':
    reports = read_input('Q2/input1.txt')
    reports = [list(map(int, report.split())) for report in reports]
    safe_report_count = sum(1 for report in reports if is_safe(report))
    print("Part 1: Number of safe reports:", safe_report_count)
    safe_report_count_modified = sum(1 for report in reports if is_safe_modified(report))
    print("Part 2: Number of safe reports with modifications:", safe_report_count_modified)
