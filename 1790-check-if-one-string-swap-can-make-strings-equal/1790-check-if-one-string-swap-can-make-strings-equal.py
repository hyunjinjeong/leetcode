class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_pos, s2_pos = [0] * len(s1), [0] * len(s2)
        
        for i in range(len(s1)):
            c1, c2 = s1[i], s2[i]
            s1_pos[i] = c1
            s2_pos[i] = c2
        
        diff = 0
        indices = []
        for i in range(len(s1)):
            if s1_pos[i] != s2_pos[i]:
                diff += 1
                indices.append(i)

        if diff == 0:
            return True
        if diff == 1 or diff > 2:
            return False
        
        return s1[indices[0]] == s2[indices[1]] and s1[indices[1]] == s2[indices[0]]