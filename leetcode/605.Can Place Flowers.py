# Suppose you have a long flowerbed in which some of the plots are planted and s
# ome are not. However, flowers cannot be planted in adjacent plots - they would c
# ompete for water and both would die. 
# 
#  Given a flowerbed (represented as an array containing 0 and 1, where 0 means 
# empty and 1 means not empty), and a number n, return if n new flowers can be pla
# nted in it without violating the no-adjacent-flowers rule. 
# 
#  Example 1: 
#  
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
#  
#  
# 
#  Example 2: 
#  
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
#  
#  
# 
#  Note: 
#  
#  The input array won't violate no-adjacent-flowers rule. 
#  The input array size is in the range of [1, 20000]. 
#  n is a non-negative integer which won't exceed the input array size. 
#  
#  Related Topics Array 
#  👍 821 👎 364

# region time
# 2020-07-25 15:45:38
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        zero = [0, 0, 0]
        res = 0
        index = 0
        if flowerbed == zero[:1]:
            return True
        if flowerbed == zero[:2]:
            return 1==n
        if flowerbed[:2] == zero[:2]:
            res += 1
            flowerbed = flowerbed[1:]
        if flowerbed[-2:] == zero[:2]:
            res += 1
            flowerbed = flowerbed[:-1]
        for _ in range(len(flowerbed) - len(zero) + 1):
            if zero == flowerbed[index:index + len(zero)]:
                res = res + 1
                flowerbed = flowerbed[index + len(zero) - 1:]
                index = 0
                continue
            index += 1
        return res >= n

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().canPlaceFlowers(flowerbed=[1,0,0,0,1,0,0], n=2))
