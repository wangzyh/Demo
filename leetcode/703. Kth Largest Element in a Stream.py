# 703. Kth Largest Element in a Stream
# Design a class to find the kth largest element in a stream. Note that it is th
# e kth largest element in the sorted order, not the kth distinct element.
#
#  Your KthLargest class will have a constructor which accepts an integer k and
# an integer array nums, which contains initial elements from the stream. For each
#  call to the method KthLargest.add, return the element representing the kth larg
# est element in the stream.
#
#  Example:
#
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
#
#
#  Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.
#  Related Topics Heap
# 2020/7/8
import bisect

class KthLargest:

    def __init__(self, k: int, nums):
        self.nums = nums
        self.nums.sort()
        self._k = k

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self._k]


if __name__ == '__main__':
    k = 3
    arr = [4, 5, 8, 2]
    kthLargest = KthLargest(3, arr)
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))

