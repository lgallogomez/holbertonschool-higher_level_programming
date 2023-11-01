def print_matrix_integer(matrix=[[]]):
    n_rows = len(matrix)
    n_columns = len(matrix[0])
    for i in range(n_rows):
        for j in range(n_columns):
            print("{:d}".format(matrix[i][j]))

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)