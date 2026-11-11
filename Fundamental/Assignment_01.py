matrix1 = []
matrix2 = []
# Input values for first matrix
print("Enter values for First Matrix:")
for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter value [{i}][{j}]: "))
        row.append(value)
    matrix1.append(row)
# Input values for second matrix
print("\nEnter values for Second Matrix:")
for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter value [{i}][{j}]: "))
        row.append(value)
    matrix2.append(row)

print("\nFirst Matrix:")
for row in matrix1:
    for value in row:
        print(value, end=" ")
    print()
# Print second matrix
print("\nSecond Matrix:")
for row in matrix2:
    for value in row:
        print(value, end=" ")
    print()
# Addition of matrices
print("\nAddition of Matrices:")
for i in range(3):
    for j in range(3):
        print(matrix1[i][j] + matrix2[i][j], end=" ")
    print()
# Subtraction of matrices
print("\nSubtraction of Matrices:")
for i in range(3):
    for j in range(3):
        print(matrix1[i][j] - matrix2[i][j], end=" ")
    print()
