import numpy as np





# Dada matriz m, número n, linha l e coluna c
# Identifica o quadro e sua respectiva matriz 3x3 
# E testa se é possível inserir n na posição.
# Retorna True/False
def TestaPossibilidade (jogo, l, c, caixa):

    possibilidade  = np.array([1,2,3,4,5,6,7,8,9]) 

    naoPossibilidade = [] 

    quadro = RetornaQuadro(jogo,caixa)
    
    for x in range (0,9):
        naoPossibilidade.append(jogo[l,x])
        naoPossibilidade.append(jogo[x,c])

    for y in range (0,3):
        naoPossibilidade.append(quadro[l%3,y])
        naoPossibilidade.append(quadro[y,c%3])

    #DEBUG
    print(f"Lista de possibilidade: {set(possibilidade).difference(naoPossibilidade)}")

    return (set(possibilidade).difference(naoPossibilidade))


    # linha = jogo[l]
    # coluna = jogo.transpose()[c]
    # quadro = RetornaMatriz(jogo,q)


   
    
    
# Dada matriz m e quadro i,
# Retorna a matriz quadro respectiva
def RetornaQuadro (m, i):
    if i == '00':
        return m[:3,:3]
    elif i == '01':
        return m[:3,3:6]
    elif i == '02':
        return m[:3,6:]

    elif i == '10':
        return m[3:6,:3]
    elif i == '11':
        return m[3:6,3:6]
    elif i == '12':
        return m[3:6,6:]
    
    elif i == '20':
        return m[6:,:3]
    elif i == '21':
        return m[6:,3:6]
    elif i == '22':
        return m[6:,6:]
    # else:
        # return m
