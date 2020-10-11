# Given an array of unique integers salary where salary[i] is the salary of the 
# employee i. 
# 
#  Return the average salary of employees excluding the minimum and maximum sala
# ry. 
# 
#  
#  Example 1: 
# 
#  
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# 
# Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500
#  
# 
#  Example 2: 
# 
#  
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# 
# Average salary excluding minimum and maximum salary is (2000)/1= 2000
#  
# 
#  Example 3: 
# 
#  
# Input: salary = [6000,5000,4000,3000,2000,1000]
# Output: 3500.00000
#  
# 
#  Example 4: 
# 
#  
# Input: salary = [8000,9000,2000,3000,6000,1000]
# Output: 4750.00000
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= salary.length <= 100 
#  10^3 <= salary[i] <= 10^6 
#  salary[i] is unique. 
#  Answers within 10^-5 of the actual value will be accepted as correct. 
#  Related Topics Array Sort 
#  👍 121 👎 26

# region time
# 2020-09-01 21:31:51
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def average(self, salary) -> float:
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [4000,3000,1000,2000]
    print(Solution().average(n))
