def solution(*args):
    count = [args.count(i) for i in args]
    return max(count) > 1