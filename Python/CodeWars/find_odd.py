def find_it(seq):
    countTuple = []
    for i in seq:
        item_exists = list(filter(lambda x: x[0] == i, countTuple))
        if item_exists:
            index_to_update = countTuple.index(item_exists[0])
            countTuple[index_to_update] = (item_exists[0][0], item_exists[0][1] + 1)
        else:
            countTuple.append((i, 1))

    return list(filter(lambda x: x[1] % 2 != 0, countTuple))[0][0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
