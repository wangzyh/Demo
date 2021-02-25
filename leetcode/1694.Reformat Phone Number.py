# You are given a phone number as a string number. number consists of digits, sp
# aces ' ', and/or dashes '-'. 
# 
#  You would like to reformat the phone number in a certain manner. Firstly, rem
# ove all spaces and dashes. Then, group the digits from left to right into blocks
#  of length 3 until there are 4 or fewer digits. The final digits are then groupe
# d as follows: 
# 
#  
#  2 digits: A single block of length 2. 
#  3 digits: A single block of length 3. 
#  4 digits: Two blocks of length 2 each. 
#  
# 
#  The blocks are then joined by dashes. Notice that the reformatting process sh
# ould never produce any blocks of length 1 and produce at most two blocks of leng
# th 2. 
# 
#  Return the phone number after formatting. 
# 
#  
#  Example 1: 
# 
#  
# Input: number = "1-23-45 6"
# Output: "123-456"
# Explanation: The digits are "123456".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st bloc
# k is "123".
# Step 2: There are 3 digits remaining, so put them in a single block of length 
# 3. The 2nd block is "456".
# Joining the blocks gives "123-456".
#  
# 
#  Example 2: 
# 
#  
# Input: number = "123 4-567"
# Output: "123-45-67"
# Explanation: The digits are "1234567".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st bloc
# k is "123".
# Step 2: There are 4 digits left, so split them into two blocks of length 2. Th
# e blocks are "45" and "67".
# Joining the blocks gives "123-45-67".
#  
# 
#  Example 3: 
# 
#  
# Input: number = "123 4-5678"
# Output: "123-456-78"
# Explanation: The digits are "12345678".
# Step 1: The 1st block is "123".
# Step 2: The 2nd block is "456".
# Step 3: There are 2 digits left, so put them in a single block of length 2. Th
# e 3rd block is "78".
# Joining the blocks gives "123-456-78".
#  
# 
#  Example 4: 
# 
#  
# Input: number = "12"
# Output: "12"
#  
# 
#  Example 5: 
# 
#  
# Input: number = "--17-5 229 35-39475 "
# Output: "175-229-353-94-75"
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= number.length <= 100 
#  number consists of digits and the characters '-' and ' '. 
#  There are at least two digits in number. 
#  
#  Related Topics String 
#  👍 86 👎 87

# region data
# 2021-02-24 14:32:41
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reformatNumber(self, number: str) -> str:
        import re
        # s = ''.join(''.join(number.split(' ')).split('-'))
        # len_3 = len(s) // 3
        # if len(s) - len_3 * 3 == 1:
        #     len_3 -= 1
        #     len_2 = 2
        # elif len(s) - len_3 * 3 == 0:
        #     len_2 = 0
        # else:
        #     len_2 = 1
        # res = []
        # for _ in range(len_3):
        #     res.append(s[:3])
        #     s = s[3:]
        # for _ in range(len_2):
        #     res.append(s[:2])
        #     s = s[2:]
        # return '-'.join(res)
        return re.sub('(...?(?=..))', r'\1-', re.sub('\D', '', number))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = "123 4-567"
    print(Solution().reformatNumber(n))
