import re

with open('AdventOfCode/Day 1/Day1Input.txt') as f:
    lines = f.read().splitlines()

def reverse(s):
    string = ""
    for i in s:
        string = i + string
    return string

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9',
    'orez': '0'
}

num=0

for string in lines:
    match=re.search(r'[0-9]|zero|one|two|three|four|five|six|seven|eight|nine',string)
    
    if match is not None:
        start,end = match.span()
        number = string[start:end]
        if len(number)==1:
            num+=10*int(number)
        else:
            num+=10*int(num_dict[number])
        
    rev_string= reverse(string)
    rev_match=re.search(r'[0-9]|orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin',rev_string)
    
    if rev_match is not None:
        start,end = rev_match.span()
        rev_number = rev_string[start:end]
        if len(rev_number)==1:
            num+=int(rev_number)
        else:
            num+=int(num_dict[rev_number])

print("num is: " + str(num))