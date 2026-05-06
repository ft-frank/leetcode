class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums)- 1):
            max_reach = max(max_reach, i + nums[i])
            if max_reach == i:
                return False
        return True
            
            

