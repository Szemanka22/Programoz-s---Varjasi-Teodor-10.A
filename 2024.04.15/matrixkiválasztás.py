l = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix = 2
oszlop = 1

def Matrixkivalasztas(matrix, oszlop):
    maxert = l[matrix][oszlop]
    maxsor = 0

    for i in range(1, len(matrix)):
        if maxert < [i][oszlop]:
            maxert = [i][oszlop]
            maxsor = i


def sorosszeg (lista):
    s = 0
    for i in range(len(lista)):
        s += lista[i]
    return(s)

def maxsorosszeg(m):
    maxert = sorosszeg(m[0])
    maxindex = 0
    for i in range(1, len(m)):
        if maxert < sorosszeg(m[i]):
            maxert = sorosszeg(m[i])
            maxindex = i

Matrixkivalasztas(matrix, oszlop)