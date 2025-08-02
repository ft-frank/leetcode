class Solution:
    def romanToInt(self, s: str) -> int:
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        def value(letter):
            if letter == "I":
                return 1
            if letter == "V":
                return 5
            if letter == "X":
                return 10
            if letter == "L":
                return 50
            if letter == "C":
                return 100
            if letter == "D":
                return 500
            if letter == "M":
                return 1000
            else:
                return 0
        output = 0
        n = len(s)
        for i in range(n):
            curr_val = value(s[i])
            if (i+1)<n and curr_val < value(s[i+1]):
                output -= curr_val
            else:
                output += curr_val
            
        return output
