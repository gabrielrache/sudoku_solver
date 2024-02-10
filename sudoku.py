# pylint: disable=C0114,C0116,C0303,C0301,C0121
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



def testa_possibilidades(jogo, l, c, modelo_menardo_caixas):

    possibilidade  = np.array([1,2,3,4,5,6,7,8,9]) 
    #sugestao = []
    nao_possibilidade = [] 
    caixa = get_box(jogo, modelo_menardo_caixas[l,c])
    
    # Method: Last Remaining Cell in a Row (or Column)
    nao_possibilidade = m_last_remaining_cell_row (jogo, l, c)
    possibilidade = (list(set(possibilidade).difference(nao_possibilidade)))
    #for element in possibilidade:
    #    if element not in nao_possibilidade:
    #        sugestao.append(element)

    # Method: Last Remaining Cell in a Box
    nao_possibilidade = m_last_remaining_cell_box (caixa)
    possibilidade = (list(set(possibilidade).difference(nao_possibilidade)))
    #for element in possibilidade:
    #    if element not in nao_possibilidade:
    #        sugestao.append(element)

    return possibilidade


# Método Last Remaining Cell in a Row
def m_last_remaining_cell_row (jogo, l, c):
    nao_possibilidade = []
    for x in range (9):
        nao_possibilidade.append(jogo[l,x])
        nao_possibilidade.append(jogo[x,c])
           
    return nao_possibilidade

# Método Last Remaining Cell in a Box
def m_last_remaining_cell_box (caixa):
    nao_possibilidade = []
    for l in range (3):
        for c in range (3):
            nao_possibilidade.append(caixa[l,c])
                        
    return nao_possibilidade


# Método Naked Candidates
def m_naked_candidates (matriz_sugestao, modelo_sesti_sudoku):
    
    ## Itera pares de sugestões
    for a in range (9):
        for b in range (9):

            ## cria tabela para marcação dos pares
            naked_pair = np.zeros((9,9), dtype=bool)

            ## Carrega matriz sugestão de cada número possível 
            mxa = matriz_sugestao[a,:,:]
            mxb = matriz_sugestao[b,:,:] 
            
            ## Ignora pares iguais onde a posição está 
            ## apenas permutada - ex.: (2,5) e (5,2)
            if a < b: 

                ## Varre linhas e colunas da matriz_sugestao procurando 
                ## células que contenham exatamente duas sugestões, alimentando
                ## a matriz naked_pair com True na posição encontrada
                for l in range (9):
                    for c in range (9):  

                        ## Teste: células com exatamente duas sugestões
                        if (matriz_sugestao[:,l,c].sum(axis=0) == 2):
                            
                            ## Teste: sugestões exatamente a e b 
                            if (mxa[l,c] == mxb[l,c] == True):  
                                
                                # DEBUG
                                # print (f"Par ({a+1}, {b+1}) detectado no [{l}, {c}]")
                                
                                # Salva posição do par 
                                naked_pair[l,c] = True
                            # fim if mxA = mxB
                        # fim if é par
                    # fim range c
                # fim range l
            # fim a<b
                
                                
            ## Localiza Naked Pairs e elimina os candidatos
            ## nas caixas, linhas e colunas 
            
            
            for x in range(9):
                naked_pair_box = get_box(naked_pair,x)
                modelo_sesti_sudoku_box = get_box(modelo_sesti_sudoku, x)
                mxa_box = get_box(mxa,x)
                mxb_box = get_box(mxb,x)
                
                ## Elimina candidatos na caixa x
                if naked_pair_box.sum() > 1:
                    for l in range (3):
                        for c in range (3):
                            if naked_pair_box[l,c] == False:
                                if mxa_box[l,c] == True:
                                    mxa_box[l,c] = False
                                    #VERBOSE
                                    print (f"{a+1} eliminado da posição {modelo_sesti_sudoku_box[l,c]}. Método: Naked Pairs - Box")
                                # fim elimina a
                                    
                                if mxb_box[l,c] == True:
                                    mxb_box[l,c] = False
                                    
                                    #VERBOSE
                                    print (f"{b+1} eliminado da posição {modelo_sesti_sudoku_box[l,c]}. Método: Naked Pairs - Box")
                                # fim elimina b
                            # fim elimina par
                        # fim range c
                    #fim range l
                # fim elimina caixa 
                
                ## Elimina candidatos na linha x
                if naked_pair[x,:].sum(axis=0) > 1:
                    for y in range (9):
                        if naked_pair[x,y] == False:
                            
                            if mxa[x,y] == True:
                                mxa[x,y] = False
                                
                                #VERBOSE
                                print (f"{a+1} eliminado da posição {modelo_sesti_sudoku[x,y]}. Método: Naked Pairs - Row")
                            # fim elimina a
                                
                            if mxb[x,y] == True:
                                mxb[x,y] = False
                                #VERBOSE
                                print (f"{b+1} eliminado da posição {modelo_sesti_sudoku[x,y]}. Método: Naked Pairs - Row")
                            # fim elimina b
                        # fim elimina par
                    # fim range y
                # fim elimina linha
                
                
                ## Elimina candidatos na coluna x
                if naked_pair[:,x].sum(axis=0) > 1:
                    for y in range (9):
                        if naked_pair[y,x] == False:
                            
                            if mxa[y,x] == True:
                                mxa[y,x] = False
                                
                                #VERBOSE
                                print (f"{a+1} eliminado da posição {modelo_sesti_sudoku[x,y]}. Método: Naked Pairs - Column")
                            # fim elimina a

                            if mxb[y,x] == True:
                                mxb[y,x] = False
                                
                                #VERBOSE
                                print (f"{b+1} eliminado da posição {modelo_sesti_sudoku[x,y]}. Método: Naked Pairs - Column")
                            # fim elimina b
                        # fim elimina par
                    # fim range y
                # fim elimina coluna
            # fim range elimina Naked pairs
            
            ## Atualiza matrizes com as caixas atualizadas
            #naked_pair = set_box(naked_pair, naked_pair_box, x)
            mxa = set_box(mxa, mxa_box, x)
            mxb = set_box(mxb, mxb_box, x)  
                            
            # Retorna matriz de sugestões atualizada
            # para matrizSugestao
            matriz_sugestao[a,:,:] = np.copy(mxa)
            matriz_sugestao[b,:,:] = np.copy(mxb)
        # fim range b
    # fim range a
                                
    return matriz_sugestao


def get_box (matriz, caixa_menardo): # apagar 10 adiante no futuro. Cuidar para ver o que quebra
    dicionario = {
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

    return dicionario.get(caixa_menardo)

def set_box (matriz, caixa, caixa_menardo):
    if caixa_menardo == 0: 
        matriz[:3 , :3] = np.copy(caixa)
    if caixa_menardo == 1: 
        matriz[:3 ,3:6] = np.copy(caixa)
    if caixa_menardo == 2: 
        matriz[:3 , 6:] = np.copy(caixa)
    if caixa_menardo == 3: 
        matriz[3:6, :3] = np.copy(caixa)
    if caixa_menardo == 4: 
        matriz[3:6,3:6] = np.copy(caixa)
    if caixa_menardo == 5: 
        matriz[3:6, 6:] = np.copy(caixa)
    if caixa_menardo == 6: 
        matriz[6: , :3] = np.copy(caixa)
    if caixa_menardo == 7: 
        matriz[6: ,3:6] = np.copy(caixa)
    if caixa_menardo == 8:         
        matriz[6: , 6:] = np.copy(caixa)
    return matriz

def atualiza_parcial (resolvido_parcial, matriz_sugestao, modelo_sesti_sudoku):

    for l in range (9):
        for c in range (9):
            if sum(matriz_sugestao[:,l,c]) == 1: 
                for x in range (9):
                    if matriz_sugestao[x,l,c] == True:
                        resolvido_parcial[l,c] = x+1
                        
                        # VERBOSE
                        print (f"A posição {modelo_sesti_sudoku[l,c]} recebeu {x+1} agora!") 
                    
    return resolvido_parcial
