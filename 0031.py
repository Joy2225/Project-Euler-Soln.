# How many different ways can £2 be made using any number of coins? (Given UK coin denominations: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p))

def coin_sums():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
    return ways[target]

print(coin_sums())

def coin_sums_recursive(target, coins, index):
    if target == 0:
        return 1
    if target < 0 or index < 0:
        return 0
    return coin_sums_recursive(target - coins[index], coins, index) + coin_sums_recursive(target, coins, index - 1)

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
print(coin_sums_recursive(target, coins, len(coins) - 1))
# 73682