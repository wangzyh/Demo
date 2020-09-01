# Given an integer array nums, find the sum of the elements between indices i an
# d j (i ≤ j), inclusive. 
# 
#  The update(i, val) function modifies nums by updating the element at index i 
# to val. 
# 
#  Example: 
# 
#  
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#  
# 
#  
#  Constraints: 
# 
#  
#  The array is only modifiable by the update function. 
#  You may assume the number of calls to update and sumRange function is distrib
# uted evenly. 
#  0 <= i <= j <= nums.length - 1 
#  
#  Related Topics Binary Indexed Tree Segment Tree 
#  👍 1375 👎 85

# region time
# 2020-08-22 00:14:26
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:

    def __init__(self, nums):
        self.l = None
        self.r = None
        self.nums = nums
        self.tree = [0] * (2**(len(nums) // 2 + 1 + (len(nums) % 2))-1)
        self.mid, self.node = 0, 0
        self.build_tree(0, len(nums))
        print(self.tree)

    def build_tree(self, start, end):
        self.l = l
        self.r = r
        self.value = 0
        self.left = None
        self.right = None
        if l < r:
            mid = (l + r) / 2
            self.left = Tree(l, mid)
            self.right = Tree(mid + 1, r)

    # def update(self, i: int, val: int) -> None:
    #     if self.start == self.end:
    #         self.nums[i] = val
    #         self.tree[self.node] = val
    #     else:
    #         mid = (self.start + self.end) // 2
    #         self.l_node = 2 * self.node + 1
    #         self.r_node = self.l_node + 1
    #         if (i >= self.start) and (i <= mid):
    #             self.update(i, val)
    #         else:
    #             self.update(arr, tree, right_node, mid + 1, end, index, val)
    #         tree[node] = tree[left_node] + tree[right_node]
    #
    # def sumRange(self, i: int, j: int) -> int:


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 3, 5]
    num = NumArray(n)
    # print(num.sumRange(0, 2))
    # print(num.update(1, 2))
    # print(num.sumRange(0, 2))
