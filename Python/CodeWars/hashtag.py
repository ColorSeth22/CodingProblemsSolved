def generate_hashtag(s):
    answerString = '#' + ''.join(s.title().split(' '))
    return answerString if len(answerString) > 1 and answerString < 141 else False