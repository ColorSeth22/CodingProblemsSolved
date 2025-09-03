def xo(s):
    xCount = 0
    oCount = 0
    xCount += s.count('x')
    xCount += s.count('X')
    oCount += s.count('o')
    oCount += s.count('O')
    return xCount == oCount
