"""
[
[1,3,1],
[1,5,1],
[4,2,1]
]

Sol.
# Find minimum path for each element
[
[1,4,5],
[2,7,6],
[6,8,7]
]

"""
matrix = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
# matrix[0][0] = 1
# matrix[0][1] = matrix[0][1]+matrix[0][0]
# matrix[0][2] = 5
# matrix[1][0] = 2
# matrix[1][1] = min(matrix[1][1] + matrix[1][0], matrix[1][1] + matrix[0][1])
# matrix[1][2] = min(matrix[1][2] + matrix[1][1], matrix[1][1] + matrix[0][2])




# print(matrix)
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if row==0 and col!=0:
            matrix[row][col]+=matrix[row][col-1]
        elif col==0 and row!=0:
            matrix[row][col] += matrix[row-1][col]
        elif row!=0 and col!=0:
            matrix[row][col]=min(matrix[row-1][col]+matrix[row][col], matrix[row][col-1]+matrix[row][col])
print(matrix[row][col])
