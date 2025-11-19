matrix = [
    [1, 2,3],
    [3, 4,4],
    [5, 6,5]
]

# trans_matrix = []
# for i in matrix:
#   for j in i:
#     print(j,end='')
#   print()
rows = len(matrix)
columns = len(matrix[0])
diagonal = []

for i in range(min(rows,columns)):
  diagonal.append(matrix[i][i])

print("Diagonal Elements:",diagonal)
print("Sum of Diagonal Elements:",sum(diagonal))
