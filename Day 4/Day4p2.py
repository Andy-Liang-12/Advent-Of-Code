import re

with open('AdventOfCode/Day 4/input.txt') as f:
    lines = f.read().splitlines()

card_wins = []

for line in lines:
    line = line.split(':')[1]
    number_arr = line.split('|')
    winning_numbers=number_arr[0].split()
    your_numbers=number_arr[1].split()
    score = 0
    for num in your_numbers:
        if num in winning_numbers:
            score+=1
    card_wins.append(score)

num_of_cards = []
for x in range(len(lines)):
    num_of_cards.append(1)


for index, card in enumerate(card_wins):
    for x in range(index+1,min(index+1+card,len(lines))):
        num_of_cards[x]+=num_of_cards[index]
print(card_wins)
print(num_of_cards)

print(sum(num_of_cards))

# current_scratchcard = 0
# total_scratchcards = 1
# scratchcards_left = 1

# while(scratchcards_left>0 and current_scratchcard<len(lines)):
#     current_scratchcard+=1
#     scratchcards_left-=1
#     line = lines[total_scratchcards].split(':')[1]
#     number_arr = line.split('|')
#     winning_numbers=number_arr[0].split()
#     your_numbers=number_arr[1].split()
#     score = 0
#     for num in your_numbers:
#         if num in winning_numbers:
#             score+=1
#     scratchcards_left+=score
#     total_scratchcards+=score
    
# print(total_scratchcards)



