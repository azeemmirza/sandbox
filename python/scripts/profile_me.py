import typing

# print functions
def print_matrix(matrix:list[list[int]]):
    for row in matrix:
        print(" ".join(map(str, row)))

    print()

def print_matrices(matrices: list[list[list[int]]]):
    for matrix in matrices:
        print_matrix(matrix)


# generator functions
def generate_matrix(rows: int, cols: int, fill=None) -> list[list[int]]:
    if fill is not None:
        return [[fill for r in range(cols)] for c in range(rows)]

    return [[j for j in range(cols)] for i in range(rows)]

def generate_matrices(count: int, rows: int, cols: int , fill = None) -> list[list[list[int]]]:
    if count is None:
        count = 1

    return [ generate_matrix(rows, cols, fill) for i in range(count)]


# validation
def is_valid_matrix(matrix: list[list[int]]) -> bool:
    rows = len(matrix)
    first_col_length = 0
    col_lengths = []

    for index, row in enumerate(matrix):
        col_length = len(row)
        col_lengths.append(col_length)

        if index == 0:
            first_col_length = col_length
            continue

        if col_length != first_col_length:
            return False

    return True

def is_same_dimensions(a: list[list[int]], b: list[list[int]]) -> bool:
    is_a_valid = is_valid_matrix(a)
    is_b_valid = is_valid_matrix(b)

    if not is_a_valid or not is_b_valid:
        return False

    a_row_length = len(a)
    b_row_length = len(b)

    if a_row_length != b_row_length:
        return False

    a_col_length = len(a[0])
    b_col_length = len(b[0])

    if a_col_length != b_col_length:
        return False

    return True



def is_square_matrix(matrix: list[list[int]]) -> bool:
    if not is_valid_matrix(matrix):
        return False

    row_length = len(matrix)
    col_length = len(matrix[0])

    return row_length == col_length

# operation
def add(a: list[list[int]], b: list[list[int]]):
    if not is_same_dimensions(a, b):
        raise Exception('Invalid dimensions, both of the matrices need to be of same dimensions')

    rows_length = len(a)
    cols_length = len(a[0])

    result = [[0 for _ in range(cols_length)] for _ in range(rows_length)]

    for r in range(rows_length):
        for c in range(cols_length):
            result[r][c] = a[r][c] + b[r][c]

    return result


def subtract(a: list[list[int]], b: list[list[int]]):
    if not is_same_dimensions(a, b):
        raise Exception('Invalid dimensions, both of the matrices need to be of same dimensions')

    rows_length = len(a)
    cols_length = len(a[0])

    result = [[0 for _ in range(cols_length)] for _ in range(rows_length)]

    for r in range(rows_length):
        for c in range(cols_length):
            result[r][c] = a[r][c] - b[r][c]

    return result

def scaler_multiply(a: list[list[int]], scalar: int):
    rows_length = len(a)
    cols_length = len(a[0])

    result = [[0 for _ in range(cols_length)] for _ in range(rows_length)]

    for r in range(rows_length):
        for c in range(cols_length):
            result[r][c] = a[r][c] * scalar

    return result


def matrix_multiply(a: list[list[int]], b: list[list[int]]):
    if not is_valid_matrix(a) or not is_valid_matrix(b):
        raise Exception('Invalid matrix input, both of the matrices need to be valid')
    
    rows_length_a = len(a)
    cols_length_a = len(a)[0]

    rows_length_b = len(b)
    cols_length_b = len(b)[0]

    result = [[0 for _ in range(cols_length_b)] for _ in range(rows_length_a)]

    for r in range(rows_length_a):
        for c in range(cols_length_b):
            result[r][c] = 0
            for k in range(cols_length_a):
                result[r][c] += a[r][k] * b[k][c]
    
    return result




def transpose(a: list[list[int]]):
    pass

def inverse(a: list[list[int]]):
    pass

def rank(a: list[list[int]]) -> int:
    pass

def determinant() -> float:
    pass

# ------------- main function -------------
def main():
    print('--------------\n title: profile_me.py\n description: to do matrix operations for profiling and benchmarking purpose\n--------------\n')
    matrix_one = generate_matrix(5, 3, 1)
    three_matrices = generate_matrices(3, 5, 5, 1)

    print_matrix(matrix_one)
    print_matrices(three_matrices)


    # testing valid matrix func
    valid_square_matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]

    invalid_matrix = [
        [1, 1, 1],
        [1, 1, 1, 1],
        [1, 1]
    ]

    valid_non_square_matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

    print('\n---1')
    print(f'first matrix | is valid: {is_valid_matrix(valid_square_matrix)}, is square: {is_square_matrix(valid_square_matrix)} ')

    print('\n---2')
    print(f'second matrix | is valid: {is_valid_matrix(invalid_matrix)}, is square: {is_square_matrix(invalid_matrix)}')

    print('\n---3')
    print(f'third matrix | is valid: {is_valid_matrix(valid_non_square_matrix)}, is square: {is_square_matrix(valid_non_square_matrix)}')

    print('\nmatrix additions:')
    matrix_ex_01 = generate_matrix(4, 2, 3)
    matrix_ex_02 = generate_matrix(4, 2, 1)

    print_matrix(add(matrix_ex_01, matrix_ex_02))



main()

