# Question Link https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true


# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------


# colunas, linhas = int(input('Colunas: ')), int(input('Linhas: '))

def primeira_metade():
    global linhas_menos_um
    for i in range(1, (linhas_menos_um), 2):
        desenho = '.|.'
        desenho = desenho * (i)
        print(desenho.center(colunas, '-'))

def segunda_metade():
    global linhas_menos_um, linhas
    for i in range(linhas_menos_um - 1, 0 , -2):
        desenho = '.|.'
        desenho = desenho * (i)
        print(desenho.center(colunas, '-'))

#RECEBE DO USUARIO
linhas, colunas = map(int, input().split())

#VALORES PADRÃO
welcome = 'WELCOME'
linhas_menos_um = int(linhas - 1)

primeira_metade()
print(welcome.center(colunas, '-'))
segunda_metade()




