"""
If s2 contains a permutation of s1.

Therefore we create a count of each letter within s1. 
Then we create a sliding window of length s2, where we count
the number of each letter.
If we match all the letters then s1 is within s2.


Test case 84.

str1 = {a: 1, b: 1, c: 1}
str2 = {b: 3}
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        str1 = {}
        str2 = {}
        matches = 0
        

        for c in s1:  
            str1[c] = str1.get(c, 0) + 1 #establish a count of each character within s1
        matches_needed = len(str1.keys()) #we need this many characters to have exact same count in both window and s1

        l = r = 0

        while r < len(s2):
            new_c = s2[r]
            str2[new_c] = str2.get(new_c, 0) + 1 #add new character
            
            if new_c in str1:
                if str1[new_c] == str2[new_c]:
                    matches += 1
                elif str2[new_c] == str1[new_c] + 1:
                    matches -=1

            if r - l + 1 > len(s1): #if length of window exceeds length of s1
                old_c = s2[l]
                str2[old_c] -= 1
                l += 1
        #PROBLEM: Only increase matches if matching, if it goes over, then decrease matches.
                if old_c in str1:
                    if str1[old_c] == str2[old_c]:
                        matches += 1
                    elif str2[old_c] == str1[old_c] - 1:
                        matches -=1

            

                
            

            #check if matches == matches_needed

            if matches == matches_needed:
                return True 
            r += 1
        return False


            

        
        
