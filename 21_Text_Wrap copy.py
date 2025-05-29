# Question Link https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true


import textwrap

def wrap(string, max_width):
    retorno = textwrap.fill(string, max_width)
    return retorno

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)