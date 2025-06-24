# Question Link
# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true


def minion_game(string):
    vogais = {'A', 'E', 'I', 'O', 'U'}
    pontos_vogais = 0
    pontos_consoantes = 0
    n = len(string)

    for i in range(n):
        if string[i] in vogais:
            pontos_vogais += n - i
        else:
            pontos_consoantes += n - i

    if pontos_vogais > pontos_consoantes:
        print(f'Kevin {pontos_vogais}')
    elif pontos_consoantes > pontos_vogais:
        print(f'Stuart {pontos_consoantes}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
