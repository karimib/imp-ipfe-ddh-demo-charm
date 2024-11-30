import random


class MPK:
    h = None

    def __init__(self, h):
        self.h = h

class MSK:
    s = None

    def __init__(self, s):
        self.s = s

class CT:
    ct0 = None
    cti = None

    def __init__(self, ct0, cti):
        self.ct0 = ct0
        self.cti = cti
        
class SKy:
    key = None

    def __init__(self, key):
        self.key = key


def vector_multiply_mod(vector1, vector2, p):
    """
    Multiplies two vectors element-wise under modulo p.

    Args:
        vector1 (list[int]): The first vector.
        vector2 (list[int]): The second vector.
        p (int): The modulus.

    Returns:
        list[int]: The resulting vector after element-wise multiplication under modulo p.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length")

    sum = 0
    for i in range(len(vector1)):
        sum += vector1[i] * vector2[i]

    return sum % p


def matrix_multiply_mod(A, B, p):
    """
    Multiplies two matrices A and B under modulo p.

    Args:
        A (list[list[int]]): The first matrix.
        B (list[list[int]]): The second matrix.
        p (int): The modulus.

    Returns:
        list[list[int]]: The resulting matrix after multiplication under modulo p.
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must match number of rows in B")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform matrix multiplication with modulo p
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % p

    return result


def vector_matrix_multiply_mod(vector, matrix, p):
    """
    Multiplies a vector by a matrix under modulo p.

    Args:
        vector (list[int]): The input vector.
        matrix (list[list[int]]): The input matrix.
        p (int): The modulus.

    Returns:
        list[int]: The resulting vector after multiplication under modulo p.
    """
    if len(vector) != len(matrix):
        raise ValueError(
            "The length of the vector must match the number of rows in the matrix"
        )

    result = [0 for _ in range(len(matrix[0]))]

    for j in range(len(matrix[0])):
        for i in range(len(vector)):
            result[j] = (result[j] + vector[i] * matrix[i][j]) % p

    return result


def modular_inverse(a, p):
    """
    Computes the modular inverse of a with respect to p using the extended Euclidean algorithm.
    Args:
        a (int): The number to invert.
        p (int): The modulus.
    Returns:
        int: The modular inverse of a modulo p.
    """
    t, new_t = 0, 1
    r, new_r = p, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise ValueError(f"{a} has no modular inverse modulo {p}")
    if t < 0:
        t += p

    return t


def generate_matrix_Lk(p, k):
    """
    Generates a matrix and a vector for the given p and k with arbitrary long integers.

    Args:
        p (int): The modulus for the modular arithmetic.
        k (int): The size of the matrix and vector.

    Returns:
        tuple: A tuple (matrix, vector), where:
            - matrix is a (k+1) x k matrix filled with random values and ones on the last row.
            - vector is a (k+1) x 1 vector with modular inverses and -1 as the last value.
    """
    # Initialize matrix and vector
    matrix = [[0 for _ in range(k)] for _ in range(k + 1)]
    vector = [0 for _ in range(k + 1)]

    for i in range(k):
        val = random.randint(1, p - 1)  # Random integer in the range [1, p-1]
        matrix[i][i] = val
        vector[i] = modular_inverse(val, p)

    # Fill the last row of the matrix with ones
    matrix[k] = [1 for _ in range(k)]
    vector[k] = -1

    return matrix, vector


def generate_matrix_Lk_AB(p, k):
    """
    Generates a matrix and a vector for the given p and k with arbitrary long integers.

    Args:
        p (int): The modulus for the modular arithmetic.
        k (int): The size of the matrix and vector.

    Returns:
        tuple: A tuple (matrix, vector), where:
            - matrix is a (k+1) x k matrix filled with random values and ones on the last row.
            - vector is a (k+1) x 1 vector with modular inverses and -1 as the last value.
    """
    # Initialize matrix and vector
    A, a = generate_matrix_Lk(p, k)
    B, b = generate_matrix_Lk(p, k)

    while inner_product_mod(b, a, p) != 1:
        B, b = generate_matrix_Lk(p, k)

    return A, a, B, b


def matrix_vector_dot(matrix, vector, p):
    """
    Computes the dot product of a matrix and a vector, reducing results modulo p.
    """
    if len(matrix[0]) != len(vector):
        raise ValueError(
            "Number of columns in the matrix must match the length of the vector"
        )

    # Compute the dot product row-wise, reducing modulo p
    result = [
        sum((row[i] * vector[i]) for i in range(len(vector))) % p for row in matrix
    ]
    return result


def vector_matrix_dot_mod(vector, matrix, p):
    """
    Computes the dot product of a vector and a matrix modulo p.

    Args:
        vector (list[int]): The input vector (1D list).
        matrix (list[list[int]]): The input matrix (2D list).
        p (int): The modulus.

    Returns:
        list[int]: Resultant vector after the dot product, reduced modulo p.

    Raises:
        ValueError: If the number of elements in the vector does not match the number of rows in the matrix.
    """
    # Ensure vector and matrix dimensions match
    if len(vector) != len(matrix[0]):
        raise ValueError(
            "Number of elements in the vector must match the number of rows in the matrix."
        )

    # Compute the dot product modulo p
    result = [sum(vector[j] * row[j] for j in range(len(vector))) % p for row in matrix]
    return result


def matrix_vector_multiply(matrix, vector):
    """
    Multiplies a matrix by a vector.

    Args:
        matrix (list[list[float]]): The input matrix.
        vector (list[float]): The input vector.

    Returns:
        list[float]: The resulting vector after multiplication.
    """
    if len(matrix[0]) != len(vector):
        raise ValueError(
            "Number of columns in the matrix must match the length of the vector"
        )

    result = [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    ]
    return result


def matrix_vector_multiply_mod(matrix, vector, p):
    """
    Multiplies a matrix by a vector.

    Args:
        matrix (list[list[float]]): The input matrix.
        vector (list[float]): The input vector.

    Returns:
        list[float]: The resulting vector after multiplication.
    """
    if len(matrix[0]) != len(vector):
        raise ValueError(
            "Number of columns in the matrix must match the length of the vector"
        )

    result = matrix_vector_multiply(matrix, vector) % p
    return result


def inner_product_mod(vector1, vector2, p):
    """
    Computes the inner product (dot product) of two vectors modulo p.

    Args:
        vector1 (list[int or float]): The first vector.
        vector2 (list[int or float]): The second vector.
        p (int): The modulus.

    Returns:
        int: The inner product of the two vectors modulo p.

    Raises:
        ValueError: If the vectors are not of the same length.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length")

    # Compute the inner product modulo p
    return sum(vector1[i] * vector2[i] for i in range(len(vector1))) % p


def transpose_vector(vector):
    """
    Transposes a vector (1D list to 2D column vector).

    Args:
        vector (list): A 1D list representing the vector.

    Returns:
        list[list]: A 2D list representing the transposed vector (column vector).
    """
    return [[element] for element in vector]


def transpose_matrix(matrix):
    """
    Transposes a given matrix.

    Args:
        matrix (list[list[int or float]]): A 2D list representing the matrix.

    Returns:
        list[list[int or float]]: The transposed matrix.
    """
    # Ensure the matrix is not empty
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")

    # Transpose the matrix
    transposed = [
        [matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))
    ]
    return transposed


def random_int_matrix(low, high, n, m):
    """
    Generates a matrix of random integers in the range [low, high) with dimensions (n, m).

    Args:
        low (int): The lower bound (inclusive).
        high (int): The upper bound (exclusive).
        n (int): Number of rows in the matrix.
        m (int): Number of columns in the matrix.

    Returns:
        list[list[int]]: A 2D list (matrix) of random integers.
    """
    return [[random.randint(low, high - 1) for _ in range(m)] for _ in range(n)]


def random_vector(low, high, n):
    """
    Generates a random vector with elements from range [a, b].

    Args:
        a (int): The lower bound (inclusive).
        b (int): The upper bound (inclusive).
        n (int): The size of the vector.

    Returns:
        list[int]: A vector (list) of random integers.
    """
    return [random.randint(low, high - 1) for _ in range(n)]


def transpose(matrix):
    """
    Transposes a given matrix.

    Args:
        matrix (list[list[float]]): The matrix to transpose.

    Returns:
        list[list[float]]: The transposed matrix.
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def dot_product(vector1, vector2):
    """
    Computes the dot product of two vectors.

    Args:
        vector1 (list[float]): The first vector.
        vector2 (list[float]): The second vector.

    Returns:
        float: The dot product of the two vectors.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length.")
    return sum(x * y for x, y in zip(vector1, vector2))


def compute_rT_AT_for_row(r_i, A):
    """
    Computes r_i^T * A^T for a single row r_i and the given matrix A.

    Args:
        r_i (list[float]): A single row vector.
        A (list[list[float]]): A 2D list representing the matrix.

    Returns:
        list[float]: Resulting vector after computing r_i^T * A^T.
    """
    # Transpose A
    A_T = transpose(A)

    # Compute dot product of r_i with each row of A^T
    result = [dot_product(r_i, row) for row in A_T]
    return result


def matrix_dot_product(A, B):
    """
    Computes the dot product of two matrices.

    Args:
        A (list[list[float]]): The first matrix.
        B (list[list[float]]): The second matrix.

    Returns:
        list[list[float]]: The resulting matrix after the dot product.

    Raises:
        ValueError: If the number of columns in A does not match the number of rows in B.
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must match number of rows in B")

    # Transpose B to make the dot product easier
    B_T = transpose(B)

    # Compute the dot product
    result = [[dot_product(row, col) for col in B_T] for row in A]
    return result


def vector_transposed_mul_matrix_mul_vector(x, F, y, p):
    # Step 1: Compute F * y (mod p)
    Fy = matrix_vector_multiply(F, y)

    # Step 2: Compute x^T * (Fy) (mod p)
    xTFy = sum((x[i] * Fy[i]) % p for i in range(len(x))) % p

    return xTFy


def scalar_multiply(vector, scalar):
    """
    Computes the dot product of two matrices.

    Args:
        vector (list[float]): The vector .
        scalar (int): The scalar.

    Returns:
        list[float]: The resulting vector after multiplication with the scalar.
    """
    return [scalar * element for element in vector]