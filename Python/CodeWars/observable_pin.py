from itertools import product
def get_pins(observed):
    return [''.join([str(s) for s in p]) for p in product(*[[[0,8],[1,2,4],[1,2,3,5],[2,3,6],[1,4,5,7],[2,4,5,6,8],[3,5,6,9],[4,7,8],[5,7,8,9,0],[6,8,9]][int(i)] for i in observed])]
print(get_pins('11'))