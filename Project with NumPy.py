import numpy as np

def add_matrices(A, B):
    return np.add(A, B)

def subtract_matrices(A, B):
    return np.subtract(A, B)

def multiply_matrices(A, B):
    return np.matmul(A, B)

def transpose_matrix(A):
    return np.transpose(A)

def determinant_matrix(A):
    return np.linalg.det(A)

def inverse_matrix(A):
    if np.linalg.det(A) != 0:
        return np.linalg.inv(A)
    else:
        return "Matrix is singular, cannot find inverse"

def eigenvalues_matrix(A):
    return np.linalg.eigvals(A)

# Example matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)

print("Addition of A and B:")
print(add_matrices(A, B))

print("Subtraction of A and B:")
print(subtract_matrices(A, B))

print("Multiplication of A and B:")
print(multiply_matrices(A, B))

print("Transpose of A:")
print(transpose_matrix(A))

print("Determinant of A:")
print(determinant_matrix(A))

print("Inverse of A:")
print(inverse_matrix(A))

print("Eigenvalues of A:")
print(eigenvalues_matrix(A))
