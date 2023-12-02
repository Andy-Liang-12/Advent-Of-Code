import re

with open('AdventOfCode/Day 2/Day2Input.txt') as f:
    lines = f.read().splitlines()

power_sum=0

def gamePowerScore(string): # Sample Input: Game 2: 3 red, 1 blue, 2 green; 1 blue, 9 green; 1 red, 10 green
    string_arr  = string.split(':')
    string_arr2 = string_arr[1].split(";")
    print(string_arr2)
    maxRed=maxGreen=maxBlue=0
    for x in string_arr2: #splitting into separate subgames
        for y in x.split(','): #split into number color pairs
            string_arr4 = y.split()
            number = int(string_arr4[0])
            color = string_arr4[1]
            if (color=='red' and number>maxRed):
                maxRed=number
            elif (color=='green' and number>maxGreen):
                maxGreen=number
            elif (color=='blue' and number>maxBlue):
                maxBlue=number
    return maxRed*maxBlue*maxGreen

for line in lines:
    power_sum+=gamePowerScore(line)

print(power_sum)