class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {1: 1, 2:2}

        def climb(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            res = climb(n-1)+ climb(n-2)

            memo[n] = res
            return res
        return climb(n)
