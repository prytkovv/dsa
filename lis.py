# Longest Increasing Subsequence
# yt: https://www.youtube.com/watch?v=cjWnW0hdF1Y
# wiki: https://en.wikipedia.org/wiki/Longest_increasing_subsequence

def lis(s):
    dp = [1] * len(s)
    for i in reversed(range(len(s) - 1)):
        for j in range(i + 1, len(s)):
            if s[j] > s[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# s = [1, 2, 4, 3]
# lis => len([1, 2, 3]) or len([1, 2, 4])
# lis(s)
