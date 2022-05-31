"""
:brief: transpose of a matrix
:param matrix: original matrix to be transposed
:return: a new matrix where the columns and rows of the original are swapped
"""
def matrix_transpose(matrix):
    return list(map(list, zip(*matrix)))