def bouncing_ball(h, bounce, window):
    count = 0
    if not 0 < bounce < 1: return -1
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1

print(bouncing_ball(10, 0.6, 10))
