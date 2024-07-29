class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0

        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            while cookie < len(s) and s[cookie] < g[child]:
                cookie += 1

            if cookie >= len(s):
                break

            child += 1
            cookie += 1
            res += 1
        
        return res