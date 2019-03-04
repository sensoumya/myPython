import numpy as np


def func(mat):
    rows, columns = mat.shape
    layers = min(rows, columns) // 2 + (min(rows, columns) & 1)
    traversed = []
    for l in range(layers):
        ring = [mat[l][j] for j in range(l, columns - l)] +\
            [mat[j][columns - l - 1] for j in range(l + 1, rows - l)] +\
            [mat[rows - l - 1][j] for j in range(columns - l - 2, l - 1, -1)] +\
            [mat[j][l] for j in range(rows - l - 2, l, -1)]
        traversed = traversed + ring
    print(traversed)


func(np.arange(1, 13).reshape(4, 3))
'''
input =array([[ 1,  2,  3],
              [ 4,  5,  6],
              [ 7,  8,  9],
              [10, 11, 12]])
output =  [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
'''
