# Question Link
# https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true

import numpy

n, m = input().split()
n_int = int(n)
matrix: list[list[int]] = []

for _ in range(n_int):
    values_str = []
    values_str = input().split()
    values_int = [int(x) for x in values_str]
    matrix.append(values_int)

_sum = numpy.sum(matrix, axis=0)
print(numpy.prod(_sum))
