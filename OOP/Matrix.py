
A = []
B = []

print("Enter Matrix A:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input()))
    A.append(row)

print("Enter Matrix B:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input()))
    B.append(row)

print("Addition:")
for i in range(3):
    for j in range(3):
        print(A[i][j] + B[i][j], end=" ")
    print()

print("Subtraction:")
for i in range(3):
    for j in range(3):
        print(A[i][j] - B[i][j], end=" ")
    print()
