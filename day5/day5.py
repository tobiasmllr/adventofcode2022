import os
import numpy as np


# load txt file as list:
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    input = f.readlines()

def get_stacks():
    # calculate number of stacks from length of first line
    nstacks = int(len(input[0]) / 4)
    stacks = []
    moves = []

    for i in range(0, nstacks):
        stacks.append([])


    for line in input:
        # format input line:
        line = line.replace('\n','')

        # gather move commands into list:
        if line.startswith('move'):
            m = line.replace('move','').replace('to','').replace('from','').split(' ')
            m = [int(c) for c in m if c != '']
            moves.append(m)

        # gather crates into stacks
        if line.strip(' ').startswith('['):
            for i, c in enumerate(line):
                c1 = c.replace('[','').replace(']','').replace(' ','')
                # if this is the crate ID, append to stack
                if c1 != '':
                    stacks[int(np.ceil(i/4)) - 1].append(c1)
    
    # reverse crate order to allow pop() on top crate
    for s in stacks:
        s.reverse()
        
    return moves, stacks

moves, stacks = get_stacks()

# apply moves
for m in moves:
    count = m[0]
    source = m[1]
    dest = m[2]

    for amt in range(0,count):
        crate = stacks[source-1].pop()
        stacks[dest-1].append(crate)

def print_top_crates():
    # print top crates:
    answer = ''
    for s in stacks:
        answer += s.pop()
    return (answer)

print(f'answer1: {print_top_crates()}')

### part 2 ####
moves,stacks = get_stacks()

# apply multi moves
for m in moves:
    print(m)
    count = m[0]
    source = m[1]
    dest = m[2]

    picked_crates = []
    for amt in range(0,count):
        picked_crates.insert(0,stacks[source-1].pop())

    for c in picked_crates:
        stacks[dest-1].append(c)

    print(stacks)

print(f'answer2: {print_top_crates()}')