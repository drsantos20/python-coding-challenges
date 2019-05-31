

"""
Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return
the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).
"""

def matrixElementsSum(matrix):
    sum = 0
    for line in range(len(matrix)):
        for column in range(len(matrix[0])):
            if line == 0 and matrix[line][column] != 0:
                sum += matrix[line][column]
            elif line == 1 and matrix[line][column] != 0 and matrix[line-1][column] != 0:
                sum += matrix[line][column]
            elif line == 2 and matrix[line][column] != 0 and matrix[line-1][column] != 0 and  matrix[line-2][column]:
                sum += matrix[line][column]
    print(sum)
    return sum

matrix = \
[[0,1,1,2],
 [0,5,0,0],
 [2,0,3,3]]

matrixElementsSum(matrix)