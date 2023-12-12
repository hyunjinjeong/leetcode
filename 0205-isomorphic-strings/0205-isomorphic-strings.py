class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dt = {}
        seen = set()
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            
            if c1 not in dt:
                if c2 in seen:
                    return False
                
                dt[c1] = c2
                seen.add(c2)
            else:
                if dt[c1] != c2:
                    return False
        
        return True