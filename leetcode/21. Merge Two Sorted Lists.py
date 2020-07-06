# 21. Merge Two Sorted Lists
# 2020/7/5


def main(l1, l2):
    """
    if l1 == None:
        return l2
    elif l2 == None:
        return l1

    l = ListNode()

    if l1.val < l2.val:
        l = l1
        l1 = l1.next
    else:
        l = l2
        l2 = l2.next
    p = l
    while (l1 and l2):
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next

    if l1:
        p.next = l1
    if l2:
        p.next = l2

    return l
"""

    l3 = l4 = ListNode()
    while (l1 and l2):
        if l1.val < l2.val:
            l3.next = ListNode(l1.val)
            l1 = l1.next
        else:
            l3.next = ListNode(l2.val)
            l2 = l2.next
        l3 = l3.next

    while l1:
        l3.next = ListNode(l1.val)
        l1 = l1.next
        l3 = l3.next

    while l2:
        l3.next = ListNode(l2.val)
        l2 = l2.next
        l3 = l3.next

    return l4.next

if __name__ == '__main__':
    """
    1->2->4, 
    1->3->4
    """
    a = main()
    print(a)

