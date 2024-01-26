import numpy as np

def init():

    global fl_debug
    global fl_verbose
    global modeloSestiSudoku 
    global modeloSestiCaixas
    global modeloMenardoSudoku
    global modeloMenardoCaixas
    global sudoku_base
    global jogo
    
    fl_debug = False
    fl_verbose = True

    # Nomenclatura Sesti (TM) 

    modeloSestiSudoku = np.array ([['A1','A2','A3','A4','A5','A6','A7','A8','A9'],
                                   ['B1','B2','B3','B4','B5','B6','B7','B8','B9'],
                                   ['C1','C2','C3','C4','C5','C6','C7','C8','C9'],
                                   ['D1','D2','D3','D4','D5','D6','D7','D8','D9'],
                                   ['E1','E2','E3','E4','E5','E6','E7','E8','E9'],
                                   ['F1','F2','F3','F4','F5','F6','F7','F8','F9'],
                                   ['G1','G2','G3','G4','G5','G6','G7','G8','G9'],
                                   ['H1','H2','H3','H4','H5','H6','H7','H8','H9'],
                                   ['I1','I2','I3','I4','I5','I6','I7','I8','I9']])

    modeloSestiCaixas = np.array ([['1','1','1','2','2','2','3','3','3'],
                                ['1','1','1','2','2','2','3','3','3'],
                                ['1','1','1','2','2','2','3','3','3'],
                                ['4','4','4','5','5','5','6','6','6'],
                                ['4','4','4','5','5','5','6','6','6'],
                                ['4','4','4','5','5','5','6','6','6'],
                                ['7','7','7','8','8','8','9','9','9'],
                                ['7','7','7','8','8','8','9','9','9'],
                                ['7','7','7','8','8','8','9','9','9']])


    # Nomenclatura Menardo open source

    modeloMenardoSudoku = np.array ([['00','01','02','03','04','05','06','07','08'],
                                    ['10','11','12','13','14','15','16','17','18'],
                                    ['20','21','22','23','24','25','26','27','28'],
                                    ['30','31','32','33','34','35','36','37','38'],
                                    ['40','41','42','43','44','45','46','47','48'],
                                    ['50','51','52','53','54','55','56','57','58'],
                                    ['60','61','62','63','64','65','66','67','68'],
                                    ['70','71','72','73','74','75','76','77','78'],
                                    ['80','81','82','83','84','85','86','87','88']])

    modeloMenardoCaixas = np.array ([['00','00','00','01','01','01','02','02','02'],
                                    ['00','00','00','01','01','01','02','02','02'],
                                    ['00','00','00','01','01','01','02','02','02'],
                                    ['10','10','10','11','11','11','12','12','12'],
                                    ['10','10','10','11','11','11','12','12','12'],
                                    ['10','10','10','11','11','11','12','12','12'],
                                    ['20','20','20','21','21','21','22','22','22'],
                                    ['20','20','20','21','21','21','22','22','22'],
                                    ['20','20','20','21','21','21','22','22','22']])

    #exemplo - Sudoku completo

    sudoku_base = np.array( [[1,2,3, 4,5,6, 7,8,9],
                            [4,5,6, 7,8,9, 1,2,3],
                            [7,8,9, 1,2,3, 4,5,6],
            
                            [2,3,4, 5,6,7, 8,9,1],
                            [5,6,7, 8,9,1, 2,3,4],
                            [8,9,1, 2,3,4, 5,6,7],
            
                            [3,4,5, 6,7,8, 9,1,2],
                            [6,7,8, 9,1,2, 3,4,5],
                            [9,1,2, 3,4,5, 6,7,8]])


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