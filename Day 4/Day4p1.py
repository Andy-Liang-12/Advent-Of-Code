import re

with open('AdventOfCode/Day 4/input.txt') as f:
    lines = f.read().splitlines()

total_points=0

for line in lines:
    line = line.split(':')[1]
    number_arr = line.split('|')
    winning_numbers=number_arr[0].split()
    your_numbers=number_arr[1].split()
    score = 0
    for num in your_numbers:
        if num in winning_numbers:
            if score==0:
                score = 1
            else:
                score = score*2
    total_points+=score
    
print(total_points)




