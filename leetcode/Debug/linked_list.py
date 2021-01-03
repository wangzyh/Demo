# Definition for singly-linked list.
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def stringToListNode(input):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


def linked_list(lines):
    for line in lines:
        line = str(line)
        node = stringToListNode(line)
        prettyPrintLinkedList(node)
