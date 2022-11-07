class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s, new_t = [], []
        
        for c in s:
            if c == "#":
                if new_s:
                    new_s.pop()
            else:
                new_s.append(c)
        
        for c in t:
            if c == "#":
                if new_t:
                    new_t.pop()
            else:
                new_t.append(c)
        
        print(new_s, new_t)
        
        return str(new_s) == str(new_t)