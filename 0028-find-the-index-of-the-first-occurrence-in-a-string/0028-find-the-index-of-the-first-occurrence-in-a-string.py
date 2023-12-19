class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, M = len(haystack), len(needle)
        for start in range(N - M + 1):
            for i in range(M):
                if needle[i] != haystack[start + i]:
                    break
                if i == M - 1:
                    return start
        
        return -1