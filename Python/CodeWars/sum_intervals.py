def sum_of_intervals(intervals):
    intervals = merge_intervals(intervals)
    return sum(end - start for start, end in intervals)

def merge_intervals(intervals):
    # sort intervals
    intervals.sort()
    merged = []

    for current in intervals:
        if not merged:
            merged.append(current)
        else:
            last = merged[-1]
            # check for overlap
            if current[0] <= last[1]:
                # merge overlapping intervals
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)

    return merged