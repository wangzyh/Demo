def main(grid):
    l1, l2, l0 = [], [], []
    for num, value in enumerate(grid):
        for n, v in enumerate(value):
            if v == 2:
                l2.append([num, n])
            elif v == 1:
                l1.append([num, n])
            elif v == 0:
                l0.append([num, n])
    if not l2:
        return -1
    for i in l2:
        print(i)
        if grid[i[0]+1][i[1]] or grid[i[0]][i[1]+1] or grid[i[0]-1][i[1]] or grid[i[0]][i[1]-1] == 1:
            print(11111)


if __name__ == '__main__':
    a = main([[2,1,1],[0,1,1],[1,0,1]])
    print(a)