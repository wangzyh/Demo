def convert(s: str, numRows: int) -> str:
    len_s = len(s)
    if s == '' or (numRows <= 1) or len_s <= 2 or (numRows >= len_s):
        return s
    res = []
    l_s = list(s)
    first_line = []
    interval = 2 * numRows - 2
    for i in range(len_s):
        n = i * interval
        if n >= len(l_s):
            break
        first_line.append(n)
        res.append(l_s[n])

    for i in range(1, numRows):
        res.append(l_s[i])
        for num in first_line:
            if (num + interval - i < len_s) and (i != numRows - 1):
                res.append(l_s[num + interval - i])
            if num + interval + i < len_s:
                res.append(l_s[num + interval + i])
    return ''.join(res)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    res = convert(s, numRows)
    print(res)
