# values = [1, 1, 5, 1, 5, 2, 4, 4]
values = [1, 1, 1, 1, 5, 2, 3, 4, 4]
res = ''
ctrl_c, ctrl_x, ctrl_v, ctrl_a = None, None, None, False

for i in values:
    if i == 1:
        if ctrl_a:
            res = 'a'
            ctrl_a = False
            continue
        res += 'a'
    # ctrl_c
    if i == 2:
        if ctrl_a:
            ctrl_c = res
    # ctrl_x
    if i == 3:
        if ctrl_a:
            ctrl_c = res
            res = ''
            ctrl_a = False
    # ctrl_v
    if i == 4:
        if ctrl_c:
            if ctrl_a:
                res = ctrl_c
                ctrl_a = False
                continue
            res += ctrl_c
    if i == 5:
        if not res:
            continue
        ctrl_a = True


print(len(res))
