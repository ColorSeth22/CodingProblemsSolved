def order(sentence):
    stringArray = sentence.split(' ')
    newArray = [n for n in range(8)]
    for word in stringArray:
        for char in word:
            try:
                if int(char):
                    newArray[int(char) - 1] = word
            except(ValueError):
                continue
    return ' '.join(newArray)