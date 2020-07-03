res = l1
res.next = l2

while True:
    if (l1 == None) and (l2 == None):
        return res
    if (l1 == None) and (l2 != None):
        while True:
            if l2 == None:
                return res
            res.val = l2.val
            l2 = l2.next
    if (l1 != None) and (l2 == None):
        while True:
            if l1 == None:
                return res
            res.val = l1.val
            l1 = l1.next
    if l1.val < l2.val:
        res.val = l1.val
        l1 = l1.next
    elif l1.val > l2.val:
        res.val = l2.val
        l2 = l2.next
    else:
        res.val = l1.val
        res.next.val = l2.val
        l2 = l2.next
        l1 = l1.next
    res = res.next
return res