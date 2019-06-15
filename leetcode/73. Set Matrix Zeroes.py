import numpy as np
def main(matrix):
    list_0 = []
    list_0_row = len(matrix[0])
    list_0_column = len(matrix)

    for i in range(list_0_column):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                list_0.append([i, j])

    # [list_0.append([i, j]) for i in range(list_0_column) for j in range(len(matrix[i])) if matrix[i][j] == 0]
    for l in list_0:
        row = l[0]
        column = l[1]

        for i in range(list_0_row):
            matrix[row][i] = 0

        for i in range(list_0_column):
            matrix[i][column] = 0

    print(matrix)


if __name__ == '__main__':
    a = main([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
])
    print(a)