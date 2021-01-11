# Given an array nums of n integers where n > 1, return an array output such tha
# t output[i] is equal to the product of all the elements of nums except nums[i]. 
# 
# 
#  Example: 
# 
#  
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#  
# 
#  Constraint: It's guaranteed that the product of the elements of any prefix or
#  suffix of the array (including the whole array) fits in a 32 bit integer. 
# 
#  Note: Please solve it without division and in O(n). 
# 
#  Follow up: 
# Could you solve it with constant space complexity? (The output array does not 
# count as extra space for the purpose of space complexity analysis.) 
#  Related Topics Array 
#  👍 6386 👎 494

# region data
# 2021-01-08 15:53:10
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums):
        # res = []
        # import math
        # for i in range(len(nums)):
        #     res.append(math.prod(nums[:i] + nums[i + 1:]))
        # return res

        # import math
        # res = {nums[0]: math.prod(nums[1:])}
        # for i in range(1, len(nums)):
        #     if nums[i] not in res:
        #         res[nums[i]] = math.prod(nums[:i] + nums[i + 1:])
        # return [res[i] for i in nums]

        # len_n = len(nums)
        # left, right = len_n * [1], len_n * [1]
        # for i in range(1, len_n):
        #     left[i] = nums[i - 1] * left[i - 1]
        #     right[len_n - 1 - i] = nums[-i] * right[-i]
        # return [left[i] * right[i] for i in range(len_n)]

        len_n = len(nums)
        res, right = len_n * [1], 1
        for i in range(1, len_n):
            res[i] = nums[i - 1] * res[i - 1]
        for i in range(len_n - 1, -1, -1):
            res[i] *= right
            print(right)
            right *= nums[i]
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 2, 3, 4]
    # n = [-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,,-1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,1,-1,]
    print(Solution().productExceptSelf(n))
