class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a+b
        return a

s = Solution()
print s.climbStairs(5)
