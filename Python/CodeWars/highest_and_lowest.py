def high_and_low(numbers):
    return str(max([int(i) for i in numbers.split(' ')])) + " " + str(min([int(i) for i in numbers.split(' ')]))