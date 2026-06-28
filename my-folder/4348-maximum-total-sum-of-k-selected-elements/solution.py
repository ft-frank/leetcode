class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse = True)
        total_sum = 0
        for i in range(k):
            if mul > 0:
                total_sum += (mul * nums[i])
                mul -= 1
            else:
                total_sum += nums[i]
        return total_sum
            
        
