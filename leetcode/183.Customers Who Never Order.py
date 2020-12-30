# Suppose that a website contains two tables, the Customers table and the Orders
#  table. Write a SQL query to find all customers who never order anything. 
# 
#  Table: Customers. 
# 
#  
# +----+-------+
# | Id | Name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
#  
# 
#  Table: Orders. 
# 
#  
# +----+------------+
# | Id | CustomerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
#  
# 
#  Using the above tables as example, return the following: 
# 
#  
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+
#  
#  👍 465 👎 51

# region data
# 2020-12-30 16:49:54
# endregion

# There is no code of Python3 type for this problem
select Name as Customers from Customers where Id not in (select CustomerId from Orders)