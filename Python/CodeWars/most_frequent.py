def top_3_words(text):
    text = ''.join([i.lower() if i not in '!@#$%^&*()_+=,./;:?-' else ' ' for i in text])
    textSplit = text.split(' ')
    tupleCount = []
    most_common = []
    for i in textSplit:
        tupleCount.append((textSplit.count(i), i))
    
    tupleCount = list(set(tupleCount))
    while len(most_common) < 3 and len(tupleCount) > 0:
        if max(tupleCount)[1] == '' or max(tupleCount)[1] == "'" or max(tupleCount)[1] == "'''":
            tupleCount.remove(max(tupleCount))
        else:
            most_common.append(max(tupleCount)[1])
            tupleCount.remove(max(tupleCount))
        
    return most_common