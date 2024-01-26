import numpy as np
import sudoku
import constants

constants.init()

fl_continuar = True


qtTurnos = 1
faltantesAnt = 0 


resolvidoParcial = np.copy(constants.jogo)


##########################
#### the game - perdi ####
##########################

while fl_continuar:

    if constants.fl_verbose: print (f"\nTurno {qtTurnos}")

    # Reseta matriz de sugestões
    matrizSugestao = np.zeros((9,9,9), dtype=bool)

    # Teste por linha e coluna
    for l in range (9):
        for c in range (9):        

            # Se encontrou um quadrado vazio
            if resolvidoParcial[l,c] == 0:
                
                if constants.fl_verbose: print(f"\nIteracao {constants.modeloSestiSudoku[l,c]}:")
                
                # Retorna uma lista de sugestões baseado nas linhas, colunas e quadro
                sugestao = sudoku.TestaPossibilidades (resolvidoParcial,l,c,constants.modeloMenardoCaixas[l,c])  

                if constants.fl_verbose: print (f"Lista sugestão: {sugestao}")
      
                ##DEBUG
                if constants.fl_debug: print(f"matrizSugestao = {matrizSugestao}")

                # Lógica passa para o jogo se for única sugestão disponível
                if len(sugestao) == 1: 
                    resolvidoParcial[l,c] = (sugestao[0])   
                    if constants.fl_verbose: print (f"A posição {constants.modeloSestiSudoku[l,c]} recebeu {sugestao[0]} agora!")    
                else:
                    for x in sugestao:
                        matrizSugestao[l,c,x-1] = True

                        if constants.fl_verbose: print(f"A posição {constants.modeloSestiSudoku[l,c]} pode ser {x}")

                if constants.fl_debug: print(matrizSugestao[0,:,:])


    matrizSugestao = sudoku.M_Naked_Candidates(matrizSugestao)


    resolvidoFinal = np.copy(resolvidoParcial)

    faltantes = (len(np.transpose(np.nonzero( np.select ( [resolvidoFinal==0], [resolvidoFinal+1],  0)))))

    # Se jogo estar completo, parar o loop
    if  faltantes == 0:
        print(f"Não falta nenhum número! :D")
        break

    # Se o jogo estiver travado, parar o loop
    if faltantesAnt >= faltantes:   
        print(f"\nAinda faltam {faltantes} números para serem encontrados, mas não foi possível avançar\n")
        break

    if (constants.fl_verbose and faltantes == 1): print(f"\nAinda falta 1 número para encontrar\n")
    elif constants.fl_verbose: print(f"\nAinda faltam {faltantes} números para serem encontrados!\n")

    if constants.fl_verbose: print(f"Progresso atual do Quebra-cabeça:\n\n{resolvidoFinal}")

    qtTurnos += 1
    faltantesAnt = faltantes
    
print(f"Progresso final do Quebra-cabeça:\n\n{resolvidoFinal}")



