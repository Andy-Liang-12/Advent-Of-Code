import re

# re.findall: Returns a list containing all matches
# re.search: Returns a Match object if there is a match anywhere in the string
# re.split: Returns a list where the string has been split at each match
# re.sub: Replaces one or many matches with a string
# re.match(): searches beginning of 1st line

with open('AdventOfCode/Day 1/Day1Input.txt') as f:
    lines = f.read().splitlines()

num=0
for str in lines:
    for char in str:
        if char.isdigit():
            num+=10*int(char)
            break
    for x in range(len(str)-1,-1,-1):
        if str[x].isdigit():
            num+=int(str[x])
            break
print(num)
        
        
        
        
