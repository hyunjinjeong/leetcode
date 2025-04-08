class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        
        first, second = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                if diff == 1:
                    first = i
                elif diff == 2:
                    second = i
                else:
                    return False
        
        return s1[first] == s2[second] and s1[second] == s2[first]