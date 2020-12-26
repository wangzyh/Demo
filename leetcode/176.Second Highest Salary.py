# Write a SQL query to get the second highest salary from the Employee table. 
# 
#  
# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
#  
# 
#  For example, given the above Employee table, the query should return 200 as t
# he second highest salary. If there is no second highest salary, then the query s
# hould return null. 
# 
#  
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+
#  
#  👍 962 👎 491

# region time
# 2020-12-25 21:36:45
# endregion

# There is no code of Python3 type for this problem
select max(Salary) as SecondHighestSalary from Employee where Salary not in (SELECT MAX(Salary) FROM Employee ORDER BY Salary)