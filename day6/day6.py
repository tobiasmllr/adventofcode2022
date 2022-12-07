import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    input = f.readlines()
input = input[0]

def find_seq(seq_len):
    for i in range(seq_len - 1, len(input)):
        seq=input[i-seq_len:i]
        if len(set(seq)) == seq_len:
            return i

print(f'answer 1: {find_seq(4)}')
print(f'answer 2: {find_seq(14)}')
