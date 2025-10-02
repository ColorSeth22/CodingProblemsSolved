import time
import sys
sys.setrecursionlimit(20000)

def locate(seq: list, value) -> bool: 
    for item in seq:
        if type(item) == list:
            if locate(item, value):
                return True
        if item == value:
            return True

    return False


deep_list = 'e'
for _ in range(5000):  # 5000 levels deep, .01 seconds
    deep_list = ['a', 'b', ['c', 'd', [deep_list]]]
start_time = time.time()
print(locate(deep_list, 'e'))
print("--- %s seconds ---" % (time.time() - start_time))