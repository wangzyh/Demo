from linked_list import ListNode, stringToListNode, prettyPrintLinkedList


def reverse_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    node = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return node


if __name__ == '__main__':
    n = stringToListNode('12345')
    prettyPrintLinkedList(reverse_list(n))
