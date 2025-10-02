def bucketize(*arr):
    # Create a list of empty buckets
    buckets = [None for _ in range(len(arr) + 1)]
    # Place each number in its corresponding bucket index based on count
    # if a number appears n times, it goes to bucket[n]
    for num in arr:
        count = arr.count(num)
        if buckets[count] is None:
            buckets[count] = [num]
        elif num not in buckets[count]:
            buckets[count].append(num)

    # Sort each bucket if it is not None
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i]) if buckets[i] is not None else None
    
    return buckets
print(bucketize(2,2,4,4,6,6,9,9,9,9))