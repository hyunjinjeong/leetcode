class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter, t_counter = collections.Counter(s), collections.Counter(t)

        for c in "abcdefghijklmnopqrstuvwxyz":
            if s_counter[c] != t_counter[c]:
                return False
        
        return True