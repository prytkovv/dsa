# Algorithm checks if list N can be divided into 2 lists of size N/2
# yt: https://www.youtube.com/watch?v=IsvocB5BJhw

def can_partition(values):
    if sum(values) % 2:
        return False
    target = sum(values) // 2
    dp = {0}
    for v in values:
        temp_dp = set()
        for d in dp:
            if v + d == target:
                return True
            temp_dp.add(d)
            temp_dp.add(v + d)
        dp = temp_dp
    return target in dp


# values = [1, 5, 11, 5]
# True
# can_partition(values)
