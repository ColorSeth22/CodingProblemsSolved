def move_zeros(lst):
    newList = []
    ZeroCount = 0
    for i in lst:
        if i == 0:
            ZeroCount += 1
        else:
            newList.append(i)
    zeroList = [0] * ZeroCount
    return newList + zeroList