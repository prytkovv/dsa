# Longest Common Subsequence
# best explanation on the internet: https://www.youtube.com/watch?v=Ua0GhsJSlWM
# wiki: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

def lcs(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in reversed(range(len(s1))):
        for j in reversed(range(len(s2))):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]


# s1 = 'hieroglyphology'
# s2 = 'michelangelo'
# lcs => len(hello) or len(higlo) or len(ieglo)
# lcs(s1, s2)
