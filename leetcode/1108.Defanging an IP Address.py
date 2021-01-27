# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#  
# 
#  A defanged IP address replaces every period "." with "[.]". 
# 
#  
#  Example 1: 
#  Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
#  Example 2: 
#  Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
#  
#  
#  Constraints: 
# 
#  
#  The given address is a valid IPv4 address. 
#  Related Topics String 
#  👍 559 👎 1039

# region time
# 2021-01-17 21:34:20
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = '1.1.1.1'
    print(Solution().defangIPaddr(n))
