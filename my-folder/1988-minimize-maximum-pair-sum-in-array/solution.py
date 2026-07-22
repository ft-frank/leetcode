class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1
        res = []
        max_sum = nums[l] + nums[r]
        while l < r:
            new_pair = (nums[l], nums[r])
            l += 1
            r -= 1
            if sum(new_pair) > max_sum:
                max_sum = sum(new_pair)
            res.append(new_pair)
        nums = res
        return max_sum
