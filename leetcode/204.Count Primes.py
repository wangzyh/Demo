# Count the number of prime numbers less than a non-negative number, n. 
# 
#  Example: 
# 
#  
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#  
#  Related Topics Hash Table Math 
#  👍 2037 👎 616

# region time
# 2020-07-25 19:14:53
# endregion

# region begin(Prohibit modification and deletion)
class Solution:
    def countPrimes(self, n: int) -> int:
        v = [0 for i in range(n + 3)]
        p = []
        for i in range(2, n):
            if v[i] == 0:
                p.append(i)
            for j in p:
                if i * j > n:
                    break
                v[i * j] = 1
                if i % j == 0:
                    break
        return len(p)


# endregion(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 2
    print(Solution().countPrimes(n))
