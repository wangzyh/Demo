null = -1


def build_tree(t, n):
    cl = cr = 0
    check = [0] * n
    if n:
        # left
        for i in range(n):
            if cl != '-':
                t[i].left = cl - 0
                check[t[i].left] = 1
            else:
                t[i].left = null
        # right
        for i in range(n):
            if cr != '-':
                t[i].right = cr - 0
                check[t[i].right] = 1
            else:
                t[i].right = null

        for i in range(n):
            if not check[i]:
                break
        root = i

    return root


def isomorphic(r1, r2):
    if (r1 == null) & (r2 == null):
        return 1
    if ((r1 == null) & (r2 != null)) | ((r1 != null) & (r2 == null)):
        return 0
    if t1[r1]


if __name__ == '__main__':
    r1 = build_tree(t1)
    r2 = build_tree(t2)

    if (isomorphic(r1, r2)):
        print("Yes\n")
    else:
        print('No\n')
