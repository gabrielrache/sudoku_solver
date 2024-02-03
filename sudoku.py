import numpy as np

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



def TestaPossibilidades (jogo, l, c, modeloMenardoCaixas):

    possibilidade  = np.array([1,2,3,4,5,6,7,8,9]) 
    naoPossibilidade = [] 
    caixa = RetornaCaixa(jogo, modeloMenardoCaixas[l,c])
    
    # Method: Last Remaining Cell in a Row (or Column)
    naoPossibilidade = M_Last_Remaining_Cell_Row (jogo, l, c)
    possibilidade = (list(set(possibilidade).difference(naoPossibilidade)))

    # Method: Last Remaining Cell in a Box
    naoPossibilidade = M_Last_Remaining_Cell_Box (caixa)
    possibilidade = (list(set(possibilidade).difference(naoPossibilidade)))

    return possibilidade


# Método Last Remaining Cell in a Row
def M_Last_Remaining_Cell_Row (jogo, l, c):
    naoPossibilidade = []
    for x in range (9):
        naoPossibilidade.append(jogo[l,x])
        naoPossibilidade.append(jogo[x,c])
           
    return naoPossibilidade

# Método Last Remaining Cell in a Box
def M_Last_Remaining_Cell_Box (caixa):
    naoPossibilidade = []
    for l in range (3):
        for c in range (3):
            naoPossibilidade.append(caixa[l,c])
                        
    return naoPossibilidade


# Método Naked Candidates
def M_Naked_Candidates (matrizSugestao):

# 1 - busca celulas com pares iguais
# 2a - isola pares iguais na linha
# 2b - limpa sugestões do par na linha
# 3a - isola pares iguais na coluna
# 3b - limpa sugestões do par na coluna
# 4a - isola pares iguais na caixa
# 4b - limpa sugestões do par na caixa

    ## Itera pares de sugestões
    for a in range (9):
        for b in range (9):

            ## cria tabela para marcação dos pares
            nakedPair = np.zeros((9,9), dtype=bool)

            ## Carrega matriz sugestão de cada número possível 
            mxA = matrizSugestao[a,:,:]
            mxB = matrizSugestao[b,:,:] 
            
            ## Ignora pares iguais onde a posição está 
            ## apenas permutada - ex.: (2,5) e (5,2)
            if a < b: 

                ## Varre linhas e colunas da matrizSugestao procurando 
                ## células que contenham exatamente duas sugestões, alimentando
                ## a matriz nakedPair com True na posição encontrada
                for l in range (9):
                    for c in range (9):  

                        ## Teste: células com exatamente duas sugestões
                        if (matrizSugestao[:,l,c].sum(axis=0) == 2):
                            
                            ## Teste: sugestões exatamente a e b 
                            if (mxA[l,c] == mxB[l,c] == True):  
                                print (f"Par ({a+1}, {b+1}) detectado no [{l}, {c}]")
                                
                                # Salva posição do par 
                                nakedPair[l,c] = True
                            # fim if mxA = mxB
                        # fim if é par
                    # fim range c
                # fim range l
            # fim a<b
                
                                
            ## Localiza Naked Pairs e elimina candidatos
            for x in range (9):

                caixa = RetornaCaixa(nakedPair,x)
                
                ## Elimina candidatos na caixa
                if caixa.sum() > 1:
                    for l in range (3):
                        for c in range (3):
                            pass
                        

                ## Elimina candidatos na linha
                if nakedPair[x,:].sum(axis=0) > 1:
                    for y in range (9):
                        if nakedPair[x,y] == False:
                            
                            if mxA[x,y] ==True:
                                mxA[x,y] = False
                                
                                #VERBOSE
                                print (f"{a+1} eliminado da posição ({x}, {y})")
                            # fim elimina a
                                
                            if mxB[x,y] ==True:
                                mxB[x,y] = False
                                #VERBOSE
                                print (f"{b+1} eliminado da posição ({x}, {y})")
                            # fim elimina b
                        # fim elimina par
                    # fim range y
                # fim elimina linha
                
                
                ## Elimina candidatos na coluna
                if nakedPair[:,x].sum(axis=0) > 1:
                    for y in range (9):
                        if nakedPair[y,x] == False:
                            
                            if mxA[y,x] ==True:
                                mxA[y,x] = False
                                
                                #VERBOSE
                                print (f"{a+1} eliminado da posição ({y}, {x})")
                            # fim elimina a

                            if mxB[y,x] ==True:
                                mxB[y,x] = False
                                
                                #VERBOSE
                                print (f"{b+1} eliminado da posição ({y}, {x})")
                            # fim elimina b
                        # fim elimina par
                    # fim range y
                # fim elimina coluna
            # fim range elimina Naked pairs
            
                            
            # Retorna matriz de sugestões atualizada
            # para matrizSugestao
            matrizSugestao[a,:,:] = mxA
            matrizSugestao[b,:,:] = mxB
        # fim range b
    # fim range a
                                
    return matrizSugestao


def RetornaCaixa (jogo, caixaMenardo):
    dict = {
        0 : jogo[:3 , :3],
        1 : jogo[:3 ,3:6],
        2 : jogo[:3 , 6:],
        3 : jogo[3:6, :3],
        4 : jogo[3:6,3:6],
        5 : jogo[3:6, 6:],
        6 : jogo[6: , :3],
        7 : jogo[6: ,3:6], 
        8 : jogo[6: , 6:],
        10 : jogo[3:6, :3],
        11 : jogo[3:6,3:6],
        12 : jogo[3:6, 6:],
        20 : jogo[6: , :3],
        21 : jogo[6: ,3:6], 
        22 : jogo[6: , 6:]}

    return dict.get(caixaMenardo)
