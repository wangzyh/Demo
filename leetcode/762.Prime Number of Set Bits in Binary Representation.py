# 
# Given two integers L and R, find the count of numbers in the range [L, R] (inc
# lusive) having a prime number of set bits in their binary representation.
#  
# (Recall that the number of set bits an integer has is the number of 1s present
#  when written in binary. For example, 21 written in binary is 10101 which has 3 
# set bits. Also, 1 is not a prime.)
#  
# 
#  Example 1: 
# Input: L = 6, R = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)
#  
# 
#  Example 2: 
# Input: L = 10, R = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
#  
# 
#  Note: 
#  L, R will be integers L <= R in the range [1, 10^6]. 
#  R - L will be at most 10000. 
#  Related Topics Bit Manipulation 
#  👍 293 👎 374

# region data
# 2021-01-20 12:28:37
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        # def isprime(n):
        #     '''check if integer n is a prime'''
        #
        #     # make sure n is a positive integer
        #     n = abs(int(n))
        #
        #     # 0 and 1 are not primes
        #     if n < 2:
        #         return 0
        #
        #     # 2 is the only even prime number
        #     if n == 2:
        #         return 1
        #
        #         # all other even numbers are not primes
        #     if not n & 1:
        #         return 0
        #
        #     # range starts with 3 and only needs to go up
        #     # the square root of n for all odd numbers
        #     for x in range(3, int(n ** 0.5) + 1, 2):
        #         if n % x == 0:
        #             return 0
        #
        #     return 1
        #
        # res = 0
        # for i in range(L, R + 1):
        #     res += isprime(bin(i).count('1'))
        # return res
        return sum(1 for i in range(L, R + 1) if bin(i).count("1") in {2, 3, 5, 7, 11, 13, 17, 19})


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    L = 6
    R = 10
    print(Solution().countPrimeSetBits(L, R))
