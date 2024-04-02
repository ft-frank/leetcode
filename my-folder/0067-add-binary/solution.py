class Solution:
    def addBinary(self, a: str, b: str) -> str:

        x = 1
        a_value = 0
        for binary in a[::-1]:
            if binary == "1":
                a_value += (int(binary) * x)
            x *= 2
        print(a_value)
        x = 1
        b_value = 0
        for binary in b[::-1]:
            if binary == "1":
                b_value += (int(binary) * x)
            x *= 2
        print(b_value)
        final = a_value + b_value
        print(final)
        return bin(final)[2:]


        
