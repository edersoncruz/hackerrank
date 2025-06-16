# Question Link
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true


def average(array):
    distinct_heights = set(array)
    sum_distict_heights = sum(distinct_heights)
    return round(sum_distict_heights / len(distinct_heights), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
