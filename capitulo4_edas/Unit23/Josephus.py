def josephus_sequence(n, k):
    sequence = []
    queue = []
    for i in range(1, n + 1):
        queue.append(i)
    
    j = 1
    while len(queue) > 1:
        item = queue.pop(0)
        if j % k == 0:
            sequence.append(item)
        else:
            queue.append(item)
        j += 1
    
    sequence.append(queue.pop(0))
    return sequence
