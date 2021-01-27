# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all ele
# ments in arr2 are also in arr1. 
# 
#  Sort the elements of arr1 such that the relative ordering of items in arr1 ar
# e the same as in arr2. Elements that don't appear in arr2 should be placed at th
# e end of arr1 in ascending order. 
# 
#  
#  Example 1: 
#  Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
#  
#  
#  Constraints: 
# 
#  
#  1 <= arr1.length, arr2.length <= 1000 
#  0 <= arr1[i], arr2[i] <= 1000 
#  All the elements of arr2 are distinct. 
#  Each arr2[i] is in arr1. 
#  
#  Related Topics Array Sort 
#  👍 934 👎 64

# region time
# 2021-01-25 23:32:35
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def relativeSortArray(self, arr1, arr2):
        from collections import Counter
        d = dict(Counter(arr1))
        res = []
        diff = []
        for i in arr2:
            res += d[i] * [i]
        for i in (set(arr1) - set(arr2)):
            diff += d[i] * [i]
        return res + sorted(diff)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 7, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(Solution().relativeSortArray(arr1, arr2))
