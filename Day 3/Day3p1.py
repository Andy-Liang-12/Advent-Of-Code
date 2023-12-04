import re

with open('AdventOfCode/Day 3/Day3Input.txt') as f:
    lines = f.read().splitlines()

# new_string = ''
# for line in lines:
#     alt = re.sub(r'[0-9]+', '', line)
#     alt2 = re.sub(r'\.','',alt)
#     new_string += alt2
    
# print("".join(set(new_string)))
part_sum = 0

symbol_dict = {} #dictionary-->line number: array of positions
number_dict = {} #dictionary-->line number: array of match objects

for i, line in enumerate(lines): #splitting into individual lines
    number_match = []
    symbol_match = []
    
    matches=re.finditer(r'[0-9]+',line)
    for match in matches:
        number_match.append(match)
    number_dict[i]=number_match
        
    symbol_matches = re.finditer(r'[^\w\.]',line)
    for match in symbol_matches:
        symbol_match.append(match.span()[0])
    symbol_dict[i]=symbol_match

def part_check_helper(number_matches, line_number):
    if symbol_dict[x]: #if there's a symbol in the line
        start,stop = number_matches.span()
        for y in range(start-1,stop+1):
            if y in symbol_dict[x]:  
                return number_matches.group()
    return 0

for line_number, number_line in number_dict.items(): #iterate through each line
    for number_matches in number_line: #iterate through each number (match object)
        for x in range(max(0,line_number-1), min(len(symbol_dict),line_number+2)): #check its line, line above and below
            number_in_question = int(part_check_helper(number_matches,x))
            if (number_in_question!=0):
                part_sum+=number_in_question
                break              

print(part_sum)


