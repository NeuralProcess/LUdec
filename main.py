import numpy as np

def lu_decompose(mat):
    rows, columns = mat.shape
    s = min(rows, columns)  # to determine s: (row by s) @ (s by colunns)
    print('rows는', rows)
    print('columns는 ', columns)
    print('s는', s)

    for k in range(s):
        x = 1 / mat[k, k]
        print('k는', k)
        for i in range(k + 1, rows):
            mat[i, k] = mat[i, k] * x
            print(i,'번째 mat는 ', mat[i, k])
        for i in range(k + 1, rows):
            for j in range(k + 1, columns):
                mat[i, j] = mat[i, j] - mat[i, k] * mat[k, j]
                print(i,'번째, ', j, '번째 mat는', mat[i, j])

    L = np.tril(mat, k=-1) + np.identity(rows)
    U = np.triu(mat, k=0)
    return L, U


mat = np.array([[1, 2, 3],
                [2, 6, 4],
                [8, 9, 1]])
L, U = lu_decompose(mat)

print(L)
print(U)