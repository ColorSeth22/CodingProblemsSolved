def flip_pancakes(stack):
    flips = []
    if stack == sorted(stack):
        return []
    while len(stack) > 0:
        biggest = stack.index(max(stack))
        flips.append(biggest)
        stack[:biggest + 1] = stack[:biggest + 1][::-1]
        flips.append(len(stack) - 1)
        stack = stack[::-1][:-1]

    to_del = []
    for i in range(len(flips) - 1):
        if flips[i] == flips[i + 1]:
            to_del.append(i)
            to_del.append(i + 1)
        elif flips[i] == 0:
            to_del.append(i)

    for i in sorted(to_del, reverse=True):
        del flips[i]

    return flips