def seq_search(S, x):
    for i in range(len(S)):
        if S[i] == x:
            return i  
    return -1  

S = [11, 37, 45, 26, 59, 28, 17, 53]
x = 53

pos = seq_search(S, x)
print(f"In S, {x} is at position {pos}.")
