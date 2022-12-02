# Advent of code challenge day 1
import os

# load txt file as list:
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    input = f.readlines()

# list of elves, one more than '\n' in input.txt
elves = [0] + [0 for i in input if i == '\n']

idx = 0
for i in input:
    if i == '\n':
        idx += 1
    else:
        elves[idx] += int(i.replace('\n', ''))

print(f'answer 1: {max(elves)}')

top3 = sorted(elves, reverse=True)[:3]
print(f'answer 2: {sum(top3)}')
