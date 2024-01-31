import numpy as np
import constants
import settings

# https://www.sudokuwiki.org/Getting_Started


### To Do List: 

## Basic Strategies
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


### Doing

# Naked Pairs


### Done!

# Last Remaining Cell in a Box
# Last Remaining Cell in a Row (or Column)


def TestaPossibilidades (jogo, l, c):

    possibilidade  = np.array([1,2,3,4,5,6,7,8,9]) 
    naoPossibilidade = [] 
    caixa = RetornaCaixa(jogo, constants.modeloMenardoCaixas[l,c])
    
    # Method: Last Remaining Cell in a Row (or Column)
    naoPossibilidade = M_Last_Remaining_Cell_Row (jogo, l, c)
    possibilidade = (list(set(possibilidade).difference(naoPossibilidade)))

    # Method: Last Remaining Cell in a Box
    naoPossibilidade = M_Last_Remaining_Cell_Box (caixa)
    possibilidade = (list(set(possibilidade).difference(naoPossibilidade)))

    return possibilidade


def M_Last_Remaining_Cell_Row (jogo, l, c):
    naoPossibilidade = []
    for x in range (9):
        naoPossibilidade.append(jogo[l,x])
        naoPossibilidade.append(jogo[x,c])

    #DEBUG
    if settings.fl_debug: print (f"O método M_Last_Remaining_Cell_Row retornou {naoPossibilidade} para a posição {l}, {c}.")
        
    return naoPossibilidade

def M_Last_Remaining_Cell_Box (caixa):
    naoPossibilidade = []
    for l in range (3):
        for c in range (3):
            naoPossibilidade.append(caixa[l,c])
    
    #DEBUG
    if settings.fl_debug: print (naoPossibilidade)
            
    return naoPossibilidade

def M_Naked_Candidates (matrizSugestao):

# 1 - busca celulas com pares iguais
# 2a - isola pares iguais na linha
# 2b - limpa sugestões do par na linha
# 3a - isola pares iguais na coluna
# 3b - limpa sugestões do par na coluna
# 4a - isola pares iguais na caixa
# 4b - limpa sugestões do par na caixa

    for a in range (9):
        for b in range (9):
            if a>=b: pass
            else:

                mxA = matrizSugestao[:,:,a]
                mxB = matrizSugestao[:,:,b] 

                # DEBUG
                if settings.fl_debug: print (f"Naked Pair: ({a},{b})\n")
                if settings.fl_debug: print (f"Matriz Sugestão: \n mxA\n({mxA}\nmxB\n{mxB})\n")

                for l in range (9):
                    for c in range (9):

                        if (mxA[l,c] == True and mxB[l,c] == True):
                            print (f"Par {a}, {b} detectado no [{l}, {c}]")



        return matrizSugestao


def RetornaCaixa (jogo, caixaMenardo):
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

    return dict.get(caixaMenardo)
