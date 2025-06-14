# Question Link
# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true


from cmath import phase

data = input()
valor_r = abs(complex(data))
valor_m = phase(complex(data))

print(valor_r)
print(valor_m)
