from itertools import permutations
perm = [''.join(p) for p in permutations("0123456789")]
print(perm[1000000-1])
