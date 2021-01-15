# We are playing the Guess Game. The game is as follows: 
# 
#  I pick a number from 1 to n. You have to guess which number I picked. 
# 
#  Every time you guess wrong, I will tell you whether the number I picked is hi
# gher or lower than your guess. 
# 
#  You call a pre-defined API int guess(int num), which returns 3 possible resul
# ts: 
# 
#  
#  -1: The number I picked is lower than your guess (i.e. pick < num). 
#  1: The number I picked is higher than your guess (i.e. pick > num). 
#  0: The number I picked is equal to your guess (i.e. pick == num). 
#  
# 
#  Return the number that I picked. 
# 
#  
#  Example 1: 
#  Input: n = 10, pick = 6
# Output: 6
#  Example 2: 
#  Input: n = 1, pick = 1
# Output: 1
#  Example 3: 
#  Input: n = 2, pick = 1
# Output: 1
#  Example 4: 
#  Input: n = 2, pick = 2
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 231 - 1 
#  1 <= pick <= n 
#  
#  Related Topics Binary Search 
#  👍 526 👎 1955

# region data
# 2021-01-15 11:30:49
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    return 0 if num == pick else 1 if num > pick else -1


# 左移一位=乘2 右移移位=除2
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        node = (left + right) >> 1
        while (g := guess(node)) != 0:
            if g == 1:
                left = node + 1
            else:
                right = node - 1
            node = (left + right) >> 1
        return node


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 2
    pick = 1
    print(Solution().guessNumber(n))
