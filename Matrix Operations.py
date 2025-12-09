# Import the libraries
import numpy as np

# Create a list
a  = [[11,12,13],[21,22,23],[31,32,33]]
print(a)
print("------------------------------------")

# Convert list to Numpy Array
# Every element is the same type
# This creates the matrix
A = np.array(a)
print(A)
print("------------------------------------")

array_dim = A.ndim
matrix_sha = A.shape
num_elems_matr = A.size
print(f"Array Dimensions: {array_dim}, Matrix Dimension: {matrix_sha}, Num of Elements in Matrix: {num_elems_matr}")
print("-----------------------------------------------------------------------------------------------------------")

# Access the element on the second row and third column

pos1 = A[1, 2]
print(f"The element of the second row and third column is {pos1}")
print("-------------------------------------------------------------")


# Access the element on the first row and first column
start = A[0][0]
print(f"The element of the second row and third column is {start}")
print("-------------------------------------------------------------")

# Access the element on the first row and first and second columns
post = A[0][0:2]
print(f"The element on the first row and first and second columns is {post}")
print("--------------------------------------------------------------------")

# Access the element on the first and second rows and third column
post = A[0:2, 2]
print(f"The the element on the first and second rows and third column is {post}")
print("------------------------------------------------------------------------")

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
print(X)
print("------------------------------------")

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)
print("------------------------------------")

# Add X and Y
Z = X + Y
print(Z)
print("------------------------------------")

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)
print("------------------------------------")

# Multiply Y with 2
Z = 2 * Y
print(Z)
print("------------------------------------")

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)
print("------------------------------------")

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
print(X)
print("------------------------------------")

# Multiply X with Y

Z = X * Y
print(Z)
print("------------------------------------")

# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
print(A)
print("------------------------------------")

# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
print(B)
print("------------------------------------")

# Calculate the dot product
Z = np.dot(A,B)
print(Z)
print("------------------------------------")


# Calculate the sine of Z
np.sin(Z)
print("------------------------------------")

# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
print(C)
print("------------------------------------")

# Get the transposed of C
print(C.T)


X=np.array([[1,0,1],[2,2,2]])
out=X[0:2,2]
print(out)
