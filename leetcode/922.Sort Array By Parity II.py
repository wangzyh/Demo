# Given an array A of non-negative integers, half of the integers in A are odd, 
# and half of the integers are even. 
# 
#  Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is e
# ven, i is even. 
# 
#  You may return any answer array that satisfies this condition. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#  
# 
#  
# 
#  Note: 
# 
#  
#  2 <= A.length <= 20000 
#  A.length % 2 == 0 
#  0 <= A[i] <= 1000 
#  
# 
#  
#  
#  Related Topics Array Sort 
#  👍 884 👎 55

# region data
# 2021-01-22 14:01:09
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortArrayByParityII(self, A):
        res = [0] * len(A)
        zero, one = 0, 1
        for i in range(len(A)):
            if A[i] % 2 == 1:
                res[one] = A[i]
                one += 2
                continue
            res[zero] = A[i]
            zero += 2
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [4, 2, 5, 7]
    print(Solution().sortArrayByParityII(n))
