# Advent of code challenge day 2
import pandas as pd
import os

input = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "input.txt"),
    header=None,
    sep=" ",
    names=('opp','me'))

def eval(opp, me):
    if opp == 'A':
        if me == 'X': return 'draw'
        elif me == 'Z': return 'loss'
        else: return 'win'
    if opp == 'B':
        if me == 'Y': return 'draw'
        elif me == 'X': return 'loss'
        else: return 'win'
    if opp == 'C':
        if me == 'Z': return 'draw'
        elif me == 'Y': return 'loss'
        else: return 'win'

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'win': 6,
    'draw': 3,
    'loss': 0,
}

score = 0
for i in input.to_dict(orient='records'):
    res = eval(i['opp'], i['me'])
    score += scores[res]
    score += scores[i['me']]

print(f'answer 1: {score}')

### Part 2 ####
def get_play(res):
    if res == 'X': return 'loss'
    if res == 'Y': return 'draw'
    if res == 'Z': return 'win'

score2 = 0
for i in input.to_dict(orient='records'):
    res = get_play(i['me'])
    
    # test which play yields the required result:
    for play in ['X', 'Y', 'Z']:
        if eval(i['opp'], play) == res: break
    
    score2 += scores[res]
    score2 += scores[play]

print(f'answer 2: {score2}')

    
