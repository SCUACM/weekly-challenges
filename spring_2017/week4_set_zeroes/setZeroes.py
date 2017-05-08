# File:        setZeroes.py
# Created by:  Tim Shur
# Date:        5/2/17
#
# Challenge Description: Write a program that takes in an MxN matrix filled
# with only 1s and 0s. Transform this matrix such that if an element is a 0,
# its entire row and column are set to 0.
#
# Algorithm: First, check if the first row and/or first column will need to be
# set to zero at the end. Then, use the first row and the first column to flag
# if a particular row or column should be set to 0. Then, run through each row
# and column, setting all entries in a row or column to 0 if the corresponding
# flag is 0. Return the output matrix.
#
# Time complexity:  O(M*N) where the matrix is size MxN.
# Space complexity: O(1) additional space


def set_zeroes(matrix):
    """Performs the set_zeroes transformation.

    This transformation is described in detail above: if an element is 0,
    set its entire row and column to 0. Note: the four loops in this function
    can me condensed to two loops!
    :param matrix: the matrix to transform
    :return: the transformed matrix
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    first_column_flag = 1  # flag for the first column
    first_row_flag = 1  # flag for the first row

    # empty matrix case
    if num_rows == 0 and num_cols == 0:
        return matrix

    # check if the first row or first column will need to be zeroed out
    for row in range(num_rows):
        if matrix[row][0] == 0:
            first_column_flag = 0
            break

    for col in range(num_cols):
        if matrix[0][col] == 0:
            first_row_flag = 0
            break

    # check each body element and set row and col flags accordingly
    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if matrix[row][col] == 0:  # if body element is zero
                matrix[0][col] = matrix[row][0] = 0  # set row and col flags

    # skip first row and first column and fill in matrix
    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if matrix[0][col] == 0 or matrix[row][0] == 0:  # if flag is set
                matrix[row][col] = 0  # set element to 0

    # fill in first column and first row if necessary
    if first_column_flag == 0:
        for row in range(num_rows):
            matrix[row][0] = 0

    if first_row_flag == 0:
        for col in range(num_cols):
            matrix[0][col] = 0

    return matrix


def print_matrix(matrix):
    """Pretty-print a given matrix.

    :param matrix: The matrix to pretty-print.
    """

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=" ")
        print()

if __name__ == "__main__":  # main running sequence
    input_matrix = [[1, 1, 1, 1],
                    [0, 1, 0, 1]]

    print("Input matrix: ")
    print_matrix(input_matrix)

    output_matrix = set_zeroes(input_matrix)

    print("\nOutput matrix:")
    print_matrix(output_matrix)
