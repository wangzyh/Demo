# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing m
# oving one unit north, south, east, or west, respectively. You start at the origi
# n (0, 0) on a 2D plane and walk on the path specified by path. 
# 
#  Return True if the path crosses itself at any point, that is, if at any time 
# you are on a location you've previously visited. Return False otherwise. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= path.length <= 10^4 
#  path will only consist of characters in {'N', 'S', 'E', 'W} 
#  
#  Related Topics String 
#  👍 160 👎 5

# region time
# 2020-09-01 22:23:26
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        node = [0, 0]
        node_list = [[0, 0], ]
        for i in path:
            if i == 'N':
                node[1] += 1
            elif i == 'E':
                node[0] += 1
            elif i == 'S':
                node[1] -= 1
            elif i == 'W':
                node[0] -= 1
            if node in node_list:
                return True
            node_list.append(node.copy())

        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 'NES'
    print(Solution().isPathCrossing(n))
