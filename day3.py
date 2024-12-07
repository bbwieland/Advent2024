# It seems like the goal of the program is just to multiply some numbers. 
# It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. 
# For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

# However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored,
#  even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

import re

with open("day3.txt") as f:
    raw_text = f.read()

mul_pattern = "mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern=mul_pattern, string=raw_text)

def evaluate_mul(mul_string: str) -> int:

    digit_subpattern = "\d{1,3}"
    matches = re.findall(pattern=digit_subpattern, string=mul_string)

    assert len(matches) == 2
    result = int(matches[0]) * int(matches[1])

    return result

mul_results = list()
for mul in matches:
    mul_result = evaluate_mul(mul_string=mul)
    mul_results.append(mul_result)

print("----- Part I -----")
print(sum(mul_results))

do_regex = "do\(\)"
dont_regex = "don't\(\)"

do_flags = [m.end(0) for m in re.finditer(pattern=do_regex, string=raw_text)]
dont_flags = [m.end(0) for m in re.finditer(pattern=dont_regex, string=raw_text)]

def get_mul_substring(mul_string: str, do: list, dont: list) -> str:

    substring = ""
    program_on = True
    for index, value in enumerate(mul_string):

        if index in do:
            program_on = True

        if index in dont:
            program_on = False

        if program_on:
            substring = substring + value

    return substring

mul_substring = get_mul_substring(mul_string=raw_text, do=do_flags, dont=dont_flags)

matches_substring = re.findall(pattern=mul_pattern, string=mul_substring)

mul_results = list()
for mul in matches_substring:
    mul_result = evaluate_mul(mul_string=mul)
    mul_results.append(mul_result)

print("----- Part II ----")
print(sum(mul_results))