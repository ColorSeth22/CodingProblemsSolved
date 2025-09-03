def spin_words(sentence):
    arrayOfWords = sentence.split(' ')
    for word in arrayOfWords:
        if len(word) >= 5:
            i = len(word) - 1
            newWord = ''
            while i >= 0:
                newWord += word[i]
                i += 1
            arrayOfWords[word] = newWord

    return ' '.join(arrayOfWords)


