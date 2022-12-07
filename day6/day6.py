import os
import numpy as np

# load txt file as list:
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    input = f.readlines()
input = input[0]

def find_seq(seq_len):
    for i in range(0,len(input)):
        if i > seq_len - 1:
            seq=input[i-seq_len:i]
            if len(set(seq)) == seq_len:
                return i

print(f'answer 1: {find_seq(4)}')

### part 2
print(f'answer 1: {find_seq(14)}')
