def setZeroes(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    stack = []
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                stack.append((row, col))
    for i in stack:
        _r = i[0]
        _c = i[1]
        # Make entire row 0
        for c in range(cols):
            matrix[_r][c] = 0
        # Make Column 0
        for r in range(rows):
            matrix[r][_c] = 0
    return matrix


print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(setZeroes([[0, 1]]))

#https://leetcode.com/problems/bulb-switcher/
