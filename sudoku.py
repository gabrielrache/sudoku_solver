import numpy as np

# https://www.sudokuwiki.org/Getting_Started

def TestaPossibilidade (jogo, l, c, caixa):

    possibilidade  = np.array([1,2,3,4,5,6,7,8,9]) 

    naoPossibilidade = [] 

    quadro = RetornaQuadro(jogo,caixa)
    
    # Method: Last Remaining Cell in a Row (or Column)
    for x in range (0,9):
        naoPossibilidade.append(jogo[l,x])
        naoPossibilidade.append(jogo[x,c])

    # Method: Last Remaining Cell in a Box
    for y in range (0,3):
        naoPossibilidade.append(quadro[l%3,y])
        naoPossibilidade.append(quadro[y,c%3])

    return (list(set(possibilidade).difference(naoPossibilidade)))

def RetornaQuadro (jogo, caixa):
    dict = {
        '00' : jogo[:3 , :3],
        '01' : jogo[:3 ,3:6],
        '02' : jogo[:3 , 6:],
        '10' : jogo[3:6, :3],
        '11' : jogo[3:6,3:6],
        '12' : jogo[3:6, 6:],
        '20' : jogo[6: , :3],
        '21' : jogo[6: ,3:6], 
        '22' : jogo[6: , 6:]}

    return dict.get(caixa)
