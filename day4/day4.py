import os
import numpy as np

# load txt file as list:
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    input = f.readlines()

def get_ranges(ln):
    pairs = ln.replace('\n','').split(',')
    ranges = []
    for elem in pairs:
        sect = elem.split('-')
        ranges.append(np.arange(int(sect[0]),int(sect[1]) + 1).tolist())

    return ranges

# sum occurances where one list completely contains the other:
sum = 0
for ln in input:
    ranges = get_ranges(ln)

    e1 = [s for s in ranges[0] if s not in ranges[1]]
    e2 = [s for s in ranges[1] if s not in ranges[0]]

    # check if all elements where removed from any of the lists during the range list check
    if (e1 == []) or (e2 == []):
        sum += 1

print(f'answer1: {sum}')

### part 2 ###
# sum occurances where the lists overlap at all:
sum = 0
for ln in input:
    ranges = get_ranges(ln)
    
    e1 = [s for s in ranges[0] if s in ranges[1]]
    e2 = [s for s in ranges[1] if s in ranges[0]]

    # check if overlap is empty. If not, sum
    if not((e1 == []) or (e2 == [])):
        sum += 1

print(f'answer2: {sum}')