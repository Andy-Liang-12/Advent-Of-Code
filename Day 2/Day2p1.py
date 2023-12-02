import re

with open('AdventOfCode/Day 2/Day2Input.txt') as f:
    lines = f.read().splitlines()

game_number=0
total_id=0

# test = "Game 2: 3 red, 1 blue, 2 green; 1 blue, 9 green; 1 red, 10 green"
# test_arr  = test.split(':')
# print(test_arr)
# test_arr2 = test_arr[1].split(";")
# print(test_arr2)
# for x in test_arr2:
#     for y in x.split(','):
#         test_arr4 = y.split()
#         print(test_arr4)

#Rule: 12 red cubes, 13 green cubes, and 14 blue cubes
def isValidGame(string): # Sample Input: Game 2: 3 red, 1 blue, 2 green; 1 blue, 9 green; 1 red, 10 green
    string_arr  = string.split(':')
    string_arr2 = string_arr[1].split(";")
    print(string_arr2)
    for x in string_arr2:
        for y in x.split(','):
            string_arr4 = y.split()
            number = int(string_arr4[0])
            color = string_arr4[1]
            if ((color=='red' and number>12) or (color=='green' and number>13) or (color=='blue' and number>14)):
                return False
    return True

for line in lines:
    game_number+=1
    if isValidGame(line):
        total_id+=game_number

print(total_id)