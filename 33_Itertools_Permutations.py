# Question Link https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations

string_ , value = input().split()
value_int = int(value)
permutations_ = list(permutations(string_, value_int))
sorted_permutations = sorted(permutations_)

for s in sorted_permutations:
    print(" ".join(map(str, s)))