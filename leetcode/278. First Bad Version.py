# 278. First Bad Version
# 2020/7/10

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        index = n//2
        while index:
            if isBadVersion(index):
                self.firstBadVersion(index//2)
            else:
                self.firstBadVersion(index+1)




if __name__ == '__main__':
    n = 5
    a = main(n)
    print(a)

