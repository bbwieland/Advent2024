from typing import List

with open("day2.txt") as f:
    raw_text = f.read()

def clean_text(raw_text: str) -> List[int]:

    text_list = raw_text.splitlines(keepends=False)

    clean_list = list()

    for sublist in text_list:
        clean_list.append(sublist.split(' '))

    for sublist in clean_list:
        for index, _ in enumerate(sublist):
            sublist[index] = int(sublist[index])

    return clean_list

data = clean_text(raw_text=raw_text)

## Part I

def check_report_safety(report: List[int]) -> bool:

    report_range = range(len(report) - 1)

    # The levels are either all increasing or all decreasing.    
    is_increasing = list()
    for value in report_range:
        if report[value + 1] > report[value]:
            is_increasing.append(True)
        if report[value + 1] < report[value]:
            is_increasing.append(False)


    # Any two adjacent levels differ by at least one and at most three. 
    is_safe_difference = list()
    for value in report_range:
        if abs(report[value + 1] - report[value]) <= 3 & abs(report[value + 1] - report[value]) >= 1:
            is_safe_difference.append(True)
        else:
            is_safe_difference.append(False)

    if (all(is_increasing) or all(item == False for item in is_increasing)) and all(is_safe_difference):
        return True
    
    else:
        return False
    
safe_reports = 0

for report in data:
    if check_report_safety(report=report):
        safe_reports += 1

print("----- Part I ------")
print(f"Number of safe reports: {safe_reports} out of {len(data):,}")

def get_sublists(main_list: List) -> List[list]:

    sublists = list()

    for index, _ in enumerate(main_list):

        list_copy = main_list.copy()
        list_copy.pop(index)
        sublists.append(list_copy)

    return sublists

safe_reports = 0

for report in data:

    if check_report_safety(report=report):
        safe_reports += 1

    if not check_report_safety(report=report):

        subreports = get_sublists(main_list=report)
        subreport_validity = list()
        for subreport in subreports:
            subreport_validity.append(check_report_safety(report=subreport))
        
        if any(subreport_validity):
            safe_reports += 1

print("----- Part II -----")
print(f"Number of safe reports: {safe_reports} out of {len(data):,}")



