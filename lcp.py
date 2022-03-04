# yt: https://www.youtube.com/watch?v=0sWShKIJoo4

def longest_common_prefix(strs):
    prefix = ''
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix


# fl is longest common prefix
longest_common_prefix(['flower', 'flow', 'flight'])
# no common prefix
longest_common_prefix(['dog', 'racecar', 'car'])
