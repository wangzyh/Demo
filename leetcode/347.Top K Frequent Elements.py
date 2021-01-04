# Given a non-empty array of integers, return the k most frequent elements. 
# 
#  Example 1: 
# 
#  
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1] 
#  
# 
#  Note: 
# 
#  
#  You may assume k is always valid, 1 ≤ k ≤ number of unique elements. 
#  Your algorithm's time complexity must be better than O(n log n), where n is t
# he array's size. 
#  It's guaranteed that the answer is unique, in other words the set of the top 
# k frequent elements is unique. 
#  You can return the answer in any order. 
#  
#  Related Topics Hash Table Heap 
#  👍 4222 👎 248

# region data
# 2021-01-04 12:42:14
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums, k: int):
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1
        # dic = sorted(dic.items(), key=lambda x: x[1])
        # lend = len(dic)
        # return [dic[lend - i - 1][0] for i in range(k)]
        from collections import Counter
        import heapq

        counter = Counter(nums)
        head, res = [], []
        for key, value in counter.items():
            head.append([-value, key])

        heapq.heapify(head)

        for _ in range(k):
            key, value = heapq.heappop(head)
            res.append(value)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1, 2, 3, 3]
    k = 3
    print(Solution().topKFrequent(nums, k))
