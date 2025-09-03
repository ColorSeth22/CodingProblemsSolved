def is_isogram(string):
    string = string.lower()
    stringArray = list(string)
    stringSet = set(stringArray)
    return len(stringSet) == len(stringArray)