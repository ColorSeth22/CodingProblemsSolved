import math
def comp(array1, array2):
    for i in range(len(array1)):
        if array1[i]*array1[i] not in array2 or math.sqrt(array2[i]) not in array1:
            return False
    return True
