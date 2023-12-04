import math as m, re

with open('AdventOfCode/Day 3/Day3Input.txt') as f:
    board = f.readlines()

chars = {(r, c): [] for r in range(140) for c in range(140) if board[r][c] not in '01234566789.'}
print(chars)

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))



