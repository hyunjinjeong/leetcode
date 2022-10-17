class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dt = {}
        for c in s:
            if c in dt:
                dt[c] += 1
            else:
                dt[c] = 1
        
        for c in t:
            if c not in dt:
                return False
            
            dt[c] -= 1
        
        return all(v == 0 for v in dt.values())