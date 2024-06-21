class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stack을 쓰면 O(n) O(n)
        s1, s2 = [], []
        
        for c in s:
            if c == "#":
                if s1:
                    s1.pop()
            else:
                s1.append(c)
        
        for c in t:
            if c == "#":
                if s2:
                    s2.pop()
            else:
                s2.append(c)
        
        if len(s1) != len(s2):
            return False
        
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                return False
    
        return True
            