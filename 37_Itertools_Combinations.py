# Question Link
# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true


from itertools import combinations

string_, value = input().split()
value_int = int(value)

for i in range(1, value_int + 1):
    combinations_ = sorted(combinations(sorted(string_), i))

    for s in combinations_:
        print("".join(s))
