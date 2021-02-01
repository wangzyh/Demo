# Given an array A of non-negative integers, return an array consisting of all t
# he even elements of A, followed by all the odd elements of A. 
# 
#  You may return any answer array that satisfies this condition. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 5000 
#  0 <= A[i] <= 5000 
#  
#  
#  Related Topics Array 
#  👍 1477 👎 82

# region data
# 2021-01-22 13:17:43
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortArrayByParity(self, A):
        # d = {}
        # for i in range(len(A)):
        #     d[i] = A[i] % 2
        # res = [i for i in sorted(d.items(), key=lambda x: x[1])]
        # return [A[i[0]] for i in res]
        return sorted(A, key=lambda x: x % 2)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [3, 1, 2, 4]
    print(Solution().sortArrayByParity(n))
