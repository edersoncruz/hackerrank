# Question Link https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

def division(a,b):
    try:
        return a // b
    except Exception as e:
        return f'Error Code: {e}'
    

number_tests = int(input())
resultados = []

for _ in range(number_tests):
    try:
        a, b = map(int, input().split())    
        resultados.append(division(a, b))
    except Exception as e:
        resultados.append(f"Error Code: {e}")

for r in resultados:
    print(r)