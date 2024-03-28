class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        true = True
        while true:
            for number in range(len(nums) - 1):
                for add in range (number + 1, len(nums)):
                    outcome = nums[number] + nums[add]
                    if outcome == target:
                        return [number, add]
    
                     
                    
                   
               
                        
            
            




        

