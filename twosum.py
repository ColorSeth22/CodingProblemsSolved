def two_sum(numbers, target):
    for i in range(len(numbers)):
        for x in range(len(numbers) - 1):
            if numbers[i] + numbers[x] == target and x != i:
                return (i, x)