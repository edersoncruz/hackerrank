# Question Link https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    linhas = []
    for i in range(size-1, -1, -1):
        esquerda = alpha[size-1:i:-1]
        centro = alpha[i:size]
        linha = '-'.join(esquerda + centro)
        linhas.append(linha.center(4*size-3, '-'))

    # Primeira metade invertida (de cima até o meio)
    for linha in linhas:
        print(linha)
    # Segunda metade (depois do meio)
    for linha in linhas[-2::-1]:
        print(linha)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)