# pylint: disable=C0114,C0116,C0303,C0301,C0121
import numpy as np
import sudoku

def main ():

    # Nomenclatura Sesti (TM) 

    modelo_sesti_sudoku = np.array ([['A1','A2','A3','A4','A5','A6','A7','A8','A9'],
                                   ['B1','B2','B3','B4','B5','B6','B7','B8','B9'],
                                   ['C1','C2','C3','C4','C5','C6','C7','C8','C9'],
                                   ['D1','D2','D3','D4','D5','D6','D7','D8','D9'],
                                   ['E1','E2','E3','E4','E5','E6','E7','E8','E9'],
                                   ['F1','F2','F3','F4','F5','F6','F7','F8','F9'],
                                   ['G1','G2','G3','G4','G5','G6','G7','G8','G9'],
                                   ['H1','H2','H3','H4','H5','H6','H7','H8','H9'],
                                   ['I1','I2','I3','I4','I5','I6','I7','I8','I9']])

    # modelo_sesti_caixas = np.array ([[1,1,1,2,2,2,3,3,3],
    #                                [1,1,1,2,2,2,3,3,3],
    #                                [1,1,1,2,2,2,3,3,3],
    #                                [4,4,4,5,5,5,6,6,6],
    #                                [4,4,4,5,5,5,6,6,6],
    #                                [4,4,4,5,5,5,6,6,6],
    #                                [7,7,7,8,8,8,9,9,9],
    #                                [7,7,7,8,8,8,9,9,9],
    #                                [7,7,7,8,8,8,9,9,9]])


    # Nomenclatura Menardo - open source

    # modelo_menardo_sudoku = np.array ([[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
    #                                  [10,11,12,13,14,15,16,17,18],
    #                                  [20,21,22,23,24,25,26,27,28],
    #                                  [30,31,32,33,34,35,36,37,38],
    #                                  [40,41,42,43,44,45,46,47,48],
    #                                  [50,51,52,53,54,55,56,57,58],
    #                                  [60,61,62,63,64,65,66,67,68],
    #                                  [70,71,72,73,74,75,76,77,78],
    #                                  [80,81,82,83,84,85,86,87,88]])

    modelo_menardo_caixas = np.array ([[ 0, 0, 0, 1, 1, 1, 2, 2, 2],
                                       [ 0, 0, 0, 1, 1, 1, 2, 2, 2],
                                       [ 0, 0, 0, 1, 1, 1, 2, 2, 2],
                                       [ 3, 3, 3, 4, 4, 4, 5, 5, 5],
                                       [ 3, 3, 3, 4, 4, 4, 5, 5, 5],
                                       [ 3, 3, 3, 4, 4, 4, 5, 5, 5],
                                       [ 6, 6, 6, 7, 7, 7, 8, 8, 8],
                                       [ 6, 6, 6, 7, 7, 7, 8, 8, 8],
                                       [ 6, 6, 6, 7, 7, 7, 8, 8, 8]])

    #exemplo - Sudoku completo

    # sudoku_base = np.array( [[1,2,3, 4,5,6, 7,8,9],
    #                         [4,5,6, 7,8,9, 1,2,3],
    #                         [7,8,9, 1,2,3, 4,5,6], 
    #                         [2,3,4, 5,6,7, 8,9,1],
    #                         [5,6,7, 8,9,1, 2,3,4],
    #                         [8,9,1, 2,3,4, 5,6,7],
    #                         [3,4,5, 6,7,8, 9,1,2],
    #                         [6,7,8, 9,1,2, 3,4,5],
    #                         [9,1,2, 3,4,5, 6,7,8]])


    ### SUDOKU - EASY

    jogo = np.array([[0,5,0, 1,0,0, 3,0,9],
                    [0,9,0, 0,2,0, 0,0,5],
                    [8,0,4, 0,0,3, 0,0,2],
                    [7,0,2, 0,0,8, 0,6,0],
                    [9,3,0, 0,7,0, 8,0,0],
                    [0,0,0, 0,9,4, 5,0,0],
                    [0,6,0, 0,0,0, 7,0,1],
                    [5,0,0, 0,7,0, 0,3,0],
                    [0,0,1, 8,3,5, 0,0,0]])



    #DUMMY

    # jogo = np.array([[0,0,0, 0,0,0, 0,0,0],
    #                  [4,0,6, 7,8,9, 1,2,3],
    #                  [7,8,9, 1,2,3, 4,5,6],
    #                  [2,3,4, 5,6,7, 8,9,1],
    #                  [5,6,7, 8,9,1, 2,3,4],
    #                  [8,9,1, 2,3,4, 5,6,7],
    #                  [3,4,5, 6,7,8, 9,1,2],
    #                  [6,7,8, 9,1,2, 3,4,5],
    #                  [9,1,2, 3,4,5, 6,7,8]])


    ### TEMPLATE

    # jogo = np.array([[0,0,0, 0,0,0, 0,0,0],
    #                  [0,0,0, 0,0,0, 0,0,0],
    #                  [0,0,0, 0,0,0, 0,0,0],
    #                  [0,0,0, 0,0,0, 0,0,0],
    #                  [0,0,0, 0,0,0, 0,0,0],
    #                  [0,0,0, 0,0,0, 0,0,0],
    #                  [0,0,0, 0,0,0, 0,0,0],
    #                  [0,0,0, 0,0,0, 0,0,0],
    #                  [0,0,0, 0,0,0, 0,0,0]])

    fl_debug = False
    fl_verbose = True
    fl_continuar = True
  
    qt_turnos = 1
    faltantes_ant = 0 

    resolvido_parcial = np.copy(jogo)

    while fl_continuar:

        if fl_verbose: 
            print (f"\nTurno {qt_turnos}")

        # Reseta matriz de sugestões
        matriz_sugestao = np.zeros((9,9,9), dtype=bool)

        # Teste por linha e coluna
        for l in range (9):
            for c in range (9):        

                # Se encontrou uma célula vazia
                if resolvido_parcial[l,c] == 0:
                    
                    if fl_verbose: 
                        print(f"\nIteração {modelo_sesti_sudoku[l,c]} ({l},{c}):")
                    
                    # Retorna uma lista de sugestões baseado nas linhas, colunas e quadro
                    sugestao = sudoku.testa_possibilidades(resolvido_parcial,l,c,modelo_menardo_caixas)  

                    if fl_verbose: 
                        print (f"Lista sugestão: {sugestao}")
        
                    ##DEBUG
                    if fl_debug: 
                        print(f"matriz_sugestao = {matriz_sugestao}")

                    # Se for única sugestão disponível preenche com aquele valor
                    if len(sugestao) == 1: 
                        resolvido_parcial[l,c] = sugestao[0] 
                        if fl_verbose: 
                            print (f"A posição {modelo_sesti_sudoku[l,c]} recebeu {sugestao[0]} agora!")   
                    # Senão cria matriz de sugestões para aquele espaço 
                    else:
                        for x in sugestao:
                            matriz_sugestao[x-1,l,c] = True

                            if fl_verbose: 
                                print(f"A posição {modelo_sesti_sudoku[l,c]} pode ser {x}")
                            



        matriz_sugestao = np.copy(sudoku.m_naked_candidates(matriz_sugestao, modelo_sesti_sudoku))
        
        resolvido_parcial = np.copy(sudoku.atualiza_parcial (resolvido_parcial, matriz_sugestao, modelo_sesti_sudoku))

        resolvido_final = np.copy(resolvido_parcial)
        
        # Pega quantidade de espaços faltantes
        faltantes = len(np.nonzero( np.select ( [resolvido_final==0], [resolvido_final+1],  0))[0])
        

        # Se jogo estar completo, parar o loop
        if  faltantes == 0:
            print("Não falta nenhum número! :D")
            break

        # Se o jogo estiver travado, parar o loop
        if faltantes_ant >= faltantes:   
            print(f"\nAinda faltam {faltantes} números para serem encontrados, mas não foi possível avançar\n")
            break

        if (fl_verbose and faltantes == 1): 
            print("\nAinda falta 1 número para encontrar\n")
        elif fl_verbose: 
            print(f"\nAinda faltam {faltantes} números para serem encontrados!\n")

        if fl_verbose: 
            print(f"Progresso atual do Quebra-cabeça:\n\n{resolvido_final}")

        qt_turnos += 1
        faltantes_ant = faltantes
        
    print(f"Progresso final do Quebra-cabeça:\n\n{resolvido_final}")
    
if __name__ == "__main__":
    main()
