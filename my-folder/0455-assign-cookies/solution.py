class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookies = 0
        child = 0
        res = 0
        while cookies < (len(s)) and child < len(g):
            if s[cookies] >= g[child]:
                res += 1
                
                child+=1
            cookies+=1
        

        return res

