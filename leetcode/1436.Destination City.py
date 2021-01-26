# You are given the array paths, where paths[i] = [cityAi, cityBi] means there e
# xists a direct path going from cityAi to cityBi. Return the destination city, th
# at is, the city without any path outgoing to another city. 
# 
#  It is guaranteed that the graph of paths forms a line without any loop, there
# fore, there will be exactly one destination city. 
# 
#  
#  Example 1: 
# 
#  
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]
# ]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which i
# s the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -
# > "Sao Paulo".
#  
# 
#  Example 2: 
# 
#  
# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".
#  
# 
#  Example 3: 
# 
#  
# Input: paths = [["A","Z"]]
# Output: "Z"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= paths.length <= 100 
#  paths[i].length == 2 
#  1 <= cityAi.length, cityBi.length <= 10 
#  cityAi != cityBi 
#  All strings consist of lowercase and uppercase English letters and the space 
# character. 
#  
#  Related Topics String 
#  👍 485 👎 29

# region data
# 2021-01-26 15:47:04
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def destCity(self, paths) -> str:
        # from collections import Counter
        # p = [j for i in paths for j in i]
        # d = Counter(p)
        # for i in paths:
        #     if d.get(i[1]) == 1:
        #         return i[1]
        return list(set([i[1] for i in paths]) - set([i[0] for i in paths]))[0]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(Solution().destCity(n))
