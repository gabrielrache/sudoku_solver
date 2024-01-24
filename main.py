import numpy as np
import sudoku


#Posições implementadas x,y

modelo = np.array ([['00','01','02','03','04','05','06','07','08'],
                    ['10','11','12','13','14','15','16','17','18'],
                    ['20','21','22','23','24','25','26','27','28'],
                    ['30','31','32','33','34','35','36','37','38'],
                    ['40','41','42','43','44','45','46','47','48'],
                    ['50','51','52','53','54','55','56','57','58'],
                    ['60','61','62','63','64','65','66','67','68'],
                    ['70','71','72','73','74','75','76','77','78'],
                    ['80','81','82','83','84','85','86','87','88']])

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


#Matriz controle - preenchimento 

validador = np.zeros((9,9), dtype=str)


#Matriz controle - possibilidades

possivel = np.empty((9,9), dtype=str)


#Matriz - jogo

jogo = np.array([[0,0,0, 0,0,0, 0,0,0],
                 [4,5,6, 7,8,9, 1,2,3],
                 [7,8,9, 1,2,3, 4,5,6],

                 [2,3,4, 5,6,7, 8,9,1],
                 [5,6,7, 8,9,1, 2,3,4],
                 [8,9,1, 2,3,4, 5,6,7],
 
                 [3,4,5, 6,7,8, 9,1,2],
                 [6,7,8, 9,1,2, 3,4,5],
                 [9,1,2, 3,4,5, 6,7,8]])

##escolhe numero   

print (jogo)

for n in range (1, 10):

##escolhe posição

    for i in range (9):
        for j in range (9):

            valido = sudoku.TestaPosicao (jogo,n,i,j)  

            if valido:
                possivel[i,j] += str(n)
                possivel[i,j] += str(n)

print (possivel)


# print (valido)





##Varredura linhas
##Varredura colunas

##Varredura quadro

