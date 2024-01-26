import numpy as np

# https://www.sudokuwiki.org/Getting_Started


### To Do List: 

## Basic Strategies
# Pinned!
# Naked Single
# Naked Pairs
# Naked Triples
# Naked Quads
# Hidden Candidates
# Intersection Removal
## Tough Strategies
# X-Wing
# Singles Chains
# Y-Wing
# Rectangle Elimination
# Swordfish
# XYZ-Wing
# BUG - Bi-Value Universal Grave
# Avoidable Rectangles


# Done!

# Last Remaining Cell in a Box
# Last Remaining Cell in a Row (or Column)


def TestaPossibilidade (jogo, l, c, caixaMenardo):

    possibilidade  = np.array([1,2,3,4,5,6,7,8,9]) 

    naoPossibilidade = [] 

    caixa = RetornaQuadro(jogo,caixaMenardo)
    
    # Method: Last Remaining Cell in a Row (or Column)
    naoPossibilidade = M_Last_Remaining_Cell_Row (jogo, l, c)
    possibilidade = (list(set(possibilidade).difference(naoPossibilidade)))

    # Method: Last Remaining Cell in a Box
    naoPossibilidade = M_Last_Remaining_Cell_Box (caixa)
    possibilidade = (list(set(possibilidade).difference(naoPossibilidade)))

    return (list(set(possibilidade).difference(naoPossibilidade)))


def M_Last_Remaining_Cell_Row (jogo, l, c):
    naoPossibilidade = []
    for x in range (0,9):
        naoPossibilidade.append(jogo[l,x])
        naoPossibilidade.append(jogo[x,c])
    return naoPossibilidade

def M_Last_Remaining_Cell_Box (caixa):
    naoPossibilidade = []
    for l in range (3):
        for c in range (3):
            naoPossibilidade.append(caixa[l,c])
    print (naoPossibilidade)
    return naoPossibilidade


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
