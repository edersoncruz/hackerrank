# Question Link https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    
    t = tuple(integer_list)
    
    print(hash(t))
