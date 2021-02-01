# 
# Given a string and an integer k, you need to reverse the first k characters fo
# r every 2k characters counting from the start of the string. If there are less t
# han k characters left, reverse all of them. If there are less than 2k but greate
# r than or equal to k characters, then reverse the first k characters and left th
# e other as original.
#  
# 
#  Example: 
#  
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#  
#  
# 
# Restrictions: 
#  
#  The string consists of lower English letters only. 
#  Length of the given string and k will in the range [1, 10000] 
#  Related Topics String 
#  👍 534 👎 1500

# region time
# 2021-01-22 22:47:00
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join([s[i:i + k][::-1] + s[i + k:i + 2 * k] for i in range(0, len(s), 2 * k)]) if k != 0 else None


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "jsfshdckioewpcimlkhjaslkjewklnckdcsacdccs"
    k = 0
    print(Solution().reverseStr(n, k))
