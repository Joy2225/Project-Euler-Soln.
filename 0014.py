def collatz_chain_length(limit):
    chain_lengths = {1: 1, 2:2}
    max_length = 0
    res = 0

    for i in range(3, limit):
        n = i
        steps = 0
        temp_chain = []

        while n not in chain_lengths:
            temp_chain.append(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            steps += 1

        total_steps = steps + chain_lengths[n]
        
        for idx, value in enumerate(temp_chain):
            chain_lengths[value] = total_steps - idx

        if total_steps > max_length:
            max_length = total_steps
            res = i

    return res

limit = 1000000
print(collatz_chain_length(limit))
# 837799