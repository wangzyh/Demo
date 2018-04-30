
def test(num):
    if num>1:
        return num*test(num-1)

    else:
        return 1


a=test(4)

print(a)
