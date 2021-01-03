# Write a SQL query to find all duplicate emails in a table named Person. 
# 
#  
# +----+---------+
# | Id | Email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
#  
# 
#  For example, your query should return the following for the above table: 
# 
#  
# +---------+
# | Email   |
# +---------+
# | a@b.com |
# +---------+
#  
# 
#  Note: All emails are in lowercase. 
#  👍 551 👎 30

# region time
# 2020-12-30 19:58:57
# endregion

# There is no code of Python3 type for this problem

SELECT Email FROM Person group by Email having count(Email) > 1;
