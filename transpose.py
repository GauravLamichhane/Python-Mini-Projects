matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
cols = len(matrix[0])

# create empty transpose matrix
transpose = [[0 for _ in range(rows)] for _ in range(cols)]

# fill transpose
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

print(transpose)
