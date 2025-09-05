def create_phone_number(n):
    firstThree = str(n[0]) + str(n[1]) + str(n[2])
    secondThree = str(n[3]) + str(n[4]) + str(n[5])
    lastFour = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    return '(' + firstThree + ') ' + secondThree + '-' + lastFour

