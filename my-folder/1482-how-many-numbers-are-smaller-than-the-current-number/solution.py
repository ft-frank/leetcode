class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    
        sorted_nums = sorted(nums)

        count = {}

        for i, n in enumerate(sorted_nums):
            if n not in count:
                count[n] = i
        return [count[num] for num in nums]
            
