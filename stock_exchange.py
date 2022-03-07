# yt: https://www.youtube.com/watch?v=1pkOgXD63yU


def get_max_profit(prices):
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        if prices[right] < prices[left]:
            left = right
        else:
            max_profit = max(max_profit, prices[right] - prices[left])
        right += 1
    return max_profit


print(get_max_profit([7, 4, 5, 3, 6, 1, 8]))
