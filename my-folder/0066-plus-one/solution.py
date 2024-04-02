class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 1
        total = 0
        digits.reverse()
        for digit in digits:
            total += (x*digit)
            x *= 10
        total +=1
    
        num = []
        for digit in str(total):
            num.append(int(digit))
        return num



            
            




        

        
        
