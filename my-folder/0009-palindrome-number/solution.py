class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        lis = list((str(x)))
        lis.reverse()
        reverse = "".join(lis)

        if number == reverse:
            return True
        else:
            return False

        
