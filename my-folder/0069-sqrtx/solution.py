import math

class Solution:
    def mySqrt(self, x: int) -> int:
        x = math.sqrt(x)
        return int(math.floor(x))
        
