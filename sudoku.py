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
    caixa = Get_Box(jogo, modeloMenardoCaixas[l,c])
    
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
def M_Naked_Candidates (matrizSugestao, modeloSestiSudoku):

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
                                
                                # DEBUG
                                # print (f"Par ({a+1}, {b+1}) detectado no [{l}, {c}]")
                                
                                # Salva posição do par 
                                nakedPair[l,c] = True
                            # fim if mxA = mxB
                        # fim if é par
                    # fim range c
                # fim range l
            # fim a<b
                
                                
            ## Localiza Naked Pairs e elimina os candidatos
            ## nas caixas, linhas e colunas 
            
            
            for x in range (9):

                nakedPair_box = Get_Box(nakedPair,x)
                modeloSestiSudoku_box = Get_Box(modeloSestiSudoku, x)
                mxA_box = Get_Box(mxA,x)
                mxB_box = Get_Box(mxB,x)
                
                ## Elimina candidatos na caixa x
                if nakedPair_box.sum() > 1:
                    for l in range (3):
                        for c in range (3):
                            if nakedPair_box[l,c] == False:
                                    
                                if mxA_box[l,c] ==True:
                                    mxA_box[l,c] = False
                                        
                                    #VERBOSE
                                    print (f"{a+1} eliminado da posição {modeloSestiSudoku_box[l,c]}. Método: Naked Pairs - Box")
                                # fim elimina a
                                    
                                if mxB_box[l,c] ==True:
                                    mxB_box[l,c] = False
                                    
                                    #VERBOSE
                                    print (f"{b+1} eliminado da posição {modeloSestiSudoku_box[l,c]}. Método: Naked Pairs - Box")
                                # fim elimina b
                            # fim elimina par
                        # fim range c
                    #fim range l
                # fim elimina caixa 
                
                ## Elimina candidatos na linha x
                if nakedPair[x,:].sum(axis=0) > 1:
                    for y in range (9):
                        if nakedPair[x,y] == False:
                            
                            if mxA[x,y] ==True:
                                mxA[x,y] = False
                                
                                #VERBOSE
                                print (f"{a+1} eliminado da posição {modeloSestiSudoku[x,y]}. Método: Naked Pairs - Row")
                            # fim elimina a
                                
                            if mxB[x,y] ==True:
                                mxB[x,y] = False
                                #VERBOSE
                                print (f"{b+1} eliminado da posição {modeloSestiSudoku[x,y]}. Método: Naked Pairs - Row")
                            # fim elimina b
                        # fim elimina par
                    # fim range y
                # fim elimina linha
                
                
                ## Elimina candidatos na coluna x
                if nakedPair[:,x].sum(axis=0) > 1:
                    for y in range (9):
                        if nakedPair[y,x] == False:
                            
                            if mxA[y,x] ==True:
                                mxA[y,x] = False
                                
                                #VERBOSE
                                print (f"{a+1} eliminado da posição {modeloSestiSudoku[x,y]}. Método: Naked Pairs - Column")
                            # fim elimina a

                            if mxB[y,x] ==True:
                                mxB[y,x] = False
                                
                                #VERBOSE
                                print (f"{b+1} eliminado da posição {modeloSestiSudoku[x,y]}. Método: Naked Pairs - Column")
                            # fim elimina b
                        # fim elimina par
                    # fim range y
                # fim elimina coluna
            # fim range elimina Naked pairs
            
            ## Atualiza matrizes com as caixas atualizadas
            nakedPair = Set_Box(nakedPair, nakedPair_box, x)
            mxA = Set_Box(mxA, mxA_box, x)
            mxB = Set_Box(mxB, mxB_box, x)  
                            
            # Retorna matriz de sugestões atualizada
            # para matrizSugestao
            matrizSugestao[a,:,:] = mxA
            matrizSugestao[b,:,:] = mxB
        # fim range b
    # fim range a
                                
    return matrizSugestao


def Get_Box (matriz, caixaMenardo):
    dict = {
        0 : matriz[:3 , :3],
        1 : matriz[:3 ,3:6],
        2 : matriz[:3 , 6:],
        3 : matriz[3:6, :3],
        4 : matriz[3:6,3:6],
        5 : matriz[3:6, 6:],
        6 : matriz[6: , :3],
        7 : matriz[6: ,3:6], 
        8 : matriz[6: , 6:],
        10 : matriz[3:6, :3],
        11 : matriz[3:6,3:6],
        12 : matriz[3:6, 6:],
        20 : matriz[6: , :3],
        21 : matriz[6: ,3:6], 
        22 : matriz[6: , 6:]}

    return dict.get(caixaMenardo)

def Set_Box (matriz, caixa, caixaMenardo):
    if caixaMenardo == 0: 
        matriz[:3 , :3] = np.copy(caixa)    
    if caixaMenardo == 1: 
        matriz[:3 ,3:6] = np.copy(caixa)
    if caixaMenardo == 2: 
        matriz[:3 , 6:] = np.copy(caixa)
    if caixaMenardo == 3: 
        matriz[3:6, :3] = np.copy(caixa)
    if caixaMenardo == 4: 
        matriz[3:6,3:6] = np.copy(caixa)
    if caixaMenardo == 5: 
        matriz[3:6, 6:] = np.copy(caixa)
    if caixaMenardo == 6: 
        matriz[6: , :3] = np.copy(caixa)
    if caixaMenardo == 7: 
        matriz[6: ,3:6] = np.copy(caixa)
    if caixaMenardo == 8:         
        matriz[6: , 6:] = np.copy(caixa)
    return (matriz)

def AtualizaParcial (resolvidoParcial, matrizSugestao, modeloSestiSudoku):

    for l in range (9):
        for c in range (9):
            if sum(matrizSugestao[:,l,c]) == 1: 
                for x in range (9):
                    if matrizSugestao[x,l,c] == True:
                        resolvidoParcial[l,c] = x+1
                        
                        # VERBOSE
                        print (f"A posição {modeloSestiSudoku[l,c]} recebeu {x+1} agora!") 
                    
    return resolvidoParcial