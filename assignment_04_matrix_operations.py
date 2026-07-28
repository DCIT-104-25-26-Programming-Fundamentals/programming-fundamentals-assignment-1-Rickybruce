# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def transpose(matrix):
    transpose_matrix = []

    for j in range(columns):
        Trow = []
        for i in range(rows):
            Trow.append(matrix[i][j])
        transpose_matrix.append(Trow)
    print("\nTransposed Matrix:")
    for row in transpose_matrix:
        print(*row)

def add_matrix(matrix1, matrix2):
    sum_matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(matrix1[i][j] + matrix2[i][j])
        sum_matrix.append(row)

    print("\nSum Matrix:")
    for row in sum_matrix:
        print(*row)

def multiply_matrix(matrix1, matrix2):
    product_matrix = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        product_matrix.append(row)

    print("\nProduct Matrix:")
    for row in product_matrix:
        print(*row)
        
def main():
    global rows, columns

    rows = int(input(" Enter number of rows: "))
    columns = int(input(" Enter number of column: "))

    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        if len(row) == columns:
            matrix.append(row)
        else:
            print(f"Please enter exactly {columns} numbers.")
            return

    transpose(matrix)

    print("\nPART B")

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    print("Enter Matrix 1")
    matrix1 = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix1.append(row)

    print("Enter Matrix 2")
    matrix2 = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix2.append(row)

    add_matrix(matrix1, matrix2)

    print("\nPART C")

    rowsA = int(input("Enter rows for Matrix A: "))
    colsA = int(input("Enter columns for Matrix A: "))

    print("Enter Matrix A")
    matrixA = []

    for i in range(rowsA):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrixA.append(row)

    rowsB = int(input("Enter rows for Matrix B: "))
    colsB = int(input("Enter columns for Matrix B: "))

    if colsA != rowsB:
        print("Matrix multiplication is not possible.")
        return

    print("Enter Matrix B")
    matrixB = []

    for i in range(rowsB):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrixB.append(row)

    multiply_matrix(matrixA, matrixB)


if __name__ == "__main__":
    main()