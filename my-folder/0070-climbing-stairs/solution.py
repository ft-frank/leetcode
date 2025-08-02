import math

class Solution:
    def climbStairs(self, n: int) -> int:
        def factorial(x):
            return math.factorial(x)
        
        def combination(n, k):
            return factorial(n) // (factorial(k) * factorial(n - k))
        
        ways = 0
        max_two_steps = n // 2
        
        for two_steps in range(max_two_steps + 1):
            one_steps = n - 2 * two_steps
            total_steps = one_steps + two_steps
            ways += combination(total_steps, two_steps)
        
        return ways
