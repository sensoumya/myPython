import numpy as np


def matrixRotation(mat, rotate_by):
    r, c = mat.shape
    layers = min(r, c) // 2
    rings = []
    for l in range(layers):
        ring = [mat[l][j] for j in range(l, c - l)]\
            + [mat[j][c - l - 1] for j in range(l + 1, r - l)]\
            + [mat[r - 1 - l][j] for j in range(c - 2 - l, l - 1, -1)]\
            + [mat[j][l] for j in range(r - 2 - l, l, -1)]
        rings.append(ring)

    for i, ring in enumerate(rings):
        rings[i] = ring[rotate_by:] + ring[:rotate_by]

    for l in range(layers):
        for j in range(l, c - l):
            mat[l][j] = rings[l][0]
            del rings[l][0]
        for j in range(l + 1, r - l):
            mat[j][c - l - 1] = rings[l][0]
            del rings[l][0]
        for j in range(c - 2 - l, l - 1, -1):
            mat[r - 1 - l][j] = rings[l][0]
            del rings[l][0]
        for j in range(r - 2 - l, l, -1):
            mat[j][l] = rings[l][0]
            del rings[l][0]

    return mat


print(matrixRotation(np.arange(1, 13).reshape(4, 3), 2))

'''
input =
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

output=
[[ 3,  6,  9],
 [ 2,  5, 12],
 [ 1,  8, 11],
 [ 4,  7, 10]]
'''
