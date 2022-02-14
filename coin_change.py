# yt: https://www.youtube.com/watch?v=H9bfqozjoqs
# wiki: https://en.wikipedia.org/wiki/Change-making_problem

def change_coins(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount]


# coins => 2
# change_coins([1, 3, 4, 5], 7)
