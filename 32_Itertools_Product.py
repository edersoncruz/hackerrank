# Question Link https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product

A = list(map(int, input().split()))  
B = list(map(int, input().split()))  

product_cartesian = list(product(A,B))

str_product = " ".join(map(str,product_cartesian))

print(str_product)
