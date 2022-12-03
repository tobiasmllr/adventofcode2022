import os

# load txt file as list:
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    input = f.readlines()

# score string, used to get letter index + 1
score_string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum = 0
for line in input:
    # format input line:
    if line == '\n': continue
    line = line.replace('\n','')

    # split string into compartments:
    c1 = line[0:len(line)//2]
    c2 = line[len(line)//2:]
    
    # find common letter
    val = [v for v in c1 if v in c2]

    # find score of letter:
    score = [i for i, v in enumerate(score_string) if v == val[0]]
    
    # sum score
    sum += score[0] + 1
    
print(f'part 1: {sum}')

### part 2 ###
groups = []
count = 0
for indx, line in enumerate(input):
    # format input line:
    if line == '\n': continue
    line = line.replace('\n','')

    # append 3 sets of the lines to one group each
    if (indx % 3) == 0:
        groups.append([set(line)])
    else:
        groups[count].append(set(line))

    if len(groups[count]) == 3:
        count += 1

sum = 0
for g in groups:
    # find common letter:
    val = [v for v in g[0] if (v in g[1]) and (v in g[2])]

    # find score for letter:
    score = [i for i, v in enumerate(score_string) if v == val[0]]

    sum += score[0] + 1

print(f'part 2: {sum}')