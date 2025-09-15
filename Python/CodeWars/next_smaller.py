def next_smaller(n):
    n = list(str(n))
    final = []
    for i in range(len(n)):
        start = n[:i] # lock in the first i digits, then the rest is chosen as follows:
        # middle should be the next smallest digit than the actual digit in the ith place out of the remaining digits
        # end should be the remaining digits, meaning as well excluding middle in descending order.
        digits = sorted(set(n[i:])) # makes a list of digits after the ith digit and then sorts
        # print(digits)
        middle = digits[digits.index(n[i])-1] #get next smallest out of remaining
        if middle > n[i]: # if the smallest number is n[i], then middle would be the greatest number. in this case you just want to skip
            # print('skip')
            continue
        end = sorted(n[i:])[::-1] # sort the values after start, including middle
        end.remove(middle) # remove middle now, this seems like the easiest way to omit it.
        final.append(int(''.join(start + [middle] + end))) # store this possibility
    final=sorted(final) #sort the possibilities
    n = int(''.join(n))
    # the next line says return the number before the inputted number in the list if it is smaller than the inputted number and if they are the same length (handles 0 cases like 097) else -1
    return final[final.index(n)-1] if final[final.index(n)-1] < n and len(str(n)) == len(str(final[final.index(n)-1])) else -1