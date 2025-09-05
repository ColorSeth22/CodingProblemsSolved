def order_weight(strng):
    splitString = strng.split(' ')
    tupleList = []
    for i in splitString:
        sum = 0
        for char in i:
            sum += int(char)
        tupleList.append((sum, i))
    sortedTupleList = sorted(tupleList)
    return ' '.join(n[1] for n in sortedTupleList)
            

print((order_weight("103 123 4444 99 2000")))