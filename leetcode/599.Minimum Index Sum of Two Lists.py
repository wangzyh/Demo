# Suppose Andy and Doris want to choose a restaurant for dinner, and they both h
# ave a list of favorite restaurants represented by strings. 
# 
#  You need to help them find out their common interest with the least list inde
# x sum. If there is a choice tie between answers, output all of them with no orde
# r requirement. You could assume there always exists an answer. 
# 
#  
#  Example 1: 
# 
#  
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Pia
# tti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
#  
# 
#  Example 2: 
# 
#  
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC
# ","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Sh
# ogun" with index sum 1 (0+1).
#  
# 
#  Example 3: 
# 
#  
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC
# ","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
#  
# 
#  Example 4: 
# 
#  
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN
# ","KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
#  
# 
#  Example 5: 
# 
#  
# Input: list1 = ["KFC"], list2 = ["KFC"]
# Output: ["KFC"]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= list1.length, list2.length <= 1000 
#  1 <= list1[i].length, list2[i].length <= 30 
#  list1[i] and list2[i] consist of spaces ' ' and English letters. 
#  All the stings of list1 are unique. 
#  All the stings of list2 are unique. 
#  
#  Related Topics Hash Table 
#  👍 724 👎 227

# region time
# 2021-01-21 22:09:08
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRestaurant(self, list1, list2):
        res = []
        list_diff = [(list2.index(list1[i]) + i, i) for i in range(len(list1)) if list1[i] in list2]
        max_l = min(list_diff, key=lambda x: x[0])[0]

        for i in sorted(list_diff, key=lambda x: x[0]):
            if i[0] != max_l:
                break
            res.append(list1[i[1]])
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    # list2 = ["Piatti", "KFC", "Hungry Hunter Steakhouse", "Shogun"]
    print(Solution().findRestaurant(list1, list2))
