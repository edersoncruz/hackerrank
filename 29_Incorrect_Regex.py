# Question Link https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
  
import re

def verificar_regex(regex):
    try:
        re.compile(regex)  # Tenta compilar a regex
        return True
    except re.error:  # Captura erros de regex inválida
        return False

test_cases = int(input())

result = []

for _ in range(test_cases):
    regex = input()
    result.append(verificar_regex(regex))

for r in result:
    print(r)