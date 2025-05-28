class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # s t를 돌고 t에서 남은 길이가 답인 듯?
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        return len(t) - j
