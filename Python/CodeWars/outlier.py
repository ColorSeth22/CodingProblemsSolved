def find_outlier(integers):
    newArray = list(filter(lambda x: x % 2 == 0, integers))
    return newArray[0] if len(newArray) == 1 else list(set(integers).difference(set(newArray)))[0] 
