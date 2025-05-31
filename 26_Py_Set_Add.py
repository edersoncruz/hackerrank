# Question Link https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
  
number_stamps = int(input())
stamps = set()

for _ in range(number_stamps):
        stamps.add((input()))

print(len(stamps))