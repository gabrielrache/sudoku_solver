import numpy as np

# Dada matriz m, número n, linha l e coluna c
# Identifica o quadro e sua respectiva matriz 3x3 
# E testa se é possível inserir n na posição.
# Retorna True/False
def TestaPosicao (jogo, l, c, quadrante):

    print (jogo)
    print(l)
    print(c)
    print(quadrante)



    # linha = jogo[l]
    # coluna = jogo.transpose()[c]
    # quadro = RetornaMatriz(jogo,q)


   
    
    
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
