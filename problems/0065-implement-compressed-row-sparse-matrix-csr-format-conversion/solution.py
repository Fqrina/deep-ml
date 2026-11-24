import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
    """
    Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

    :param dense_matrix: 2D list representing a dense matrix
    :return: A tuple containing (values array, column indices array, row pointer array)
    """
    value = []
    column = []
    rowumn = [0]
    for row in range(len(dense_matrix)):
        rowcount = 0
        for col in range(len(dense_matrix)):
            if dense_matrix[row][col] != 0:
                value.append(dense_matrix[row][col])
                column.append(col)
                rowcount+=1
        rowumn.append(rowumn[-1]+rowcount)

    return value, column, rowumn

