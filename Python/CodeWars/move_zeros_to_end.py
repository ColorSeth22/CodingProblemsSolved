import math

# def get_min_base(number, base=2):
#     # Determine the minimum base that doesn't contain zeros
#     # Recursive, create the binary representation in base n
#     # check if contains zero, if not then return that base, else recurse to the next base
#     editableNumber = number
#     if editableNumber == 0:
#         return [0]
#     digits = []
#     while editableNumber:
#         if str(editableNumber % base).count('1') != len(str(editableNumber % base)):
#             print('restart', str(editableNumber % base))
#             return get_min_base(number, base + 1)
#         else:
#             digits.append(str(editableNumber % base))
#         editableNumber //= base
#     binary = ''.join(digits[::-1])
#     if binary.count('1') != len(binary):
#         return get_min_base(number, base + 1)
#     else:
#         print(binary, base)
#         return base

def get_min_base(number):
    # geometric sequence approach
    for k in range(int(math.log2(number)) + 1, 0, -1):
        low = 2
        high = number
        while low <= high:
            # utilize binary search, not fun
            mid = (low + high) // 2
            total = 0
            for i in range(k + 1):
                # geometric sequence to find total
                total = total * mid + 1
                if total > number:
                    break
            if total == number:
                # return lowest base
                return mid
            elif total < number:
                # move the left pointer to the middle
                low = mid + 1
            else:
                # move the right pointer to the middle
                high = mid - 1

print('base:', get_min_base(1111))