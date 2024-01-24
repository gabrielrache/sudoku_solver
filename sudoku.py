import numpy as np

# Dada matriz m, número n, linha l e coluna c
# Identifica o quadro e sua respectiva matriz 3x3 
# E testa se é possível inserir n na posição.
# Retorna True/False
def TestaPosicao (m, n, l, c):

    q = RetornaQuadro(l,c)
    linha = m[l]
    coluna = m.transpose()[c]
    quadro = RetornaMatriz(m,q)

    ##verbose
    # print('Número: ', n)
    # print('Linha: ', linha)
    # print('Coluna: ', coluna)
    # print('Quadro: ', q, '\n', quadro)   

    # print('Qtd na linha: ', linha[linha==n].size)
    # print('Qtd na coluna: ', coluna[coluna==n].size)
    # print('Qtd no quadro: ', quadro[quadro==n].size)
    
    if linha[linha==n].size == 0 and coluna[coluna==n].size == 0 and quadro[quadro==n].size == 0:
        return True
    else:
        return False



# Dada linha l e coluna c,
# Retorna o nome do quadro
def RetornaQuadro (l, c):
    if l <=2 and c <= 2:
        return 'A'
    elif l <=2 and c > 2 and c <= 5:
        return 'B'
    elif l <=2 and c > 5:
        return 'C'
    
    elif l > 2 and l <= 5 and c <= 2:
        return 'D'
    elif l > 2 and l <= 5 and c > 2 and c <= 5:
        return 'E'
    elif l > 2 and l <= 5 and c > 5:
        return 'F'
    
    elif l > 5 and c <= 2:
        return 'G'
    elif l > 5 and c > 2 and c <= 5:
        return 'H'
    elif l > 5 and c > 5:
        return 'I'
    else:
        return 'X'
    
# Dada matriz m e quadro i,
# Retorna a matriz quadro respectiva
def RetornaMatriz (m, i):
    if i == 'A':
        return m[:3,:3]
    elif i == 'B':
        return m[:3,3:6]
    elif i == 'C':
        return m[:3,6:]

    elif i == 'D':
        return m[3:6,:3]
    elif i == 'E':
        return m[3:6,3:6]
    elif i == 'F':
        return m[3:6,6:]
    
    elif i == 'G':
        return m[6:,:3]
    elif i == 'H':
        return m[6:,3:6]
    elif i == 'I':
        return m[6:,6:]
    else:
        return m
