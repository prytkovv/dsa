# wiki: https://en.wikipedia.org/wiki/Edit_distance
# yt: https://www.youtube.com/watch?v=XYi2-LPrwm4&t=1044s


def edit_distance(s1, s2):
    dp = [[float('inf')] * (len(s2) + 1)for _ in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        dp[i][len(s2)] = len(s1) - i
    for j in range(len(s2) + 1):
        dp[len(s1)][j] = len(s2) - j
    for i in reversed(range(len(s1))):
        for j in reversed(range(len(s2))):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1
    return dp[0][0]


# abcde -> abce = 2 steps
# edit_distance('abc', 'abcde')
