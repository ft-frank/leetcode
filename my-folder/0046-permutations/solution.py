"""
When encountering an index we can 
1. Append it, move onto next.
2. Don't append it, move onto next, leave it avaliable to be added

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        cur = []
        used = set()
        

        def permute(cur, used):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in used:
                    cur.append(nums[i])
                    used.add(nums[i])
                    permute(cur, used)

                    used.remove(nums[i])
                    cur.pop()
        permute(cur, used)
        return res






      
            

            
            
