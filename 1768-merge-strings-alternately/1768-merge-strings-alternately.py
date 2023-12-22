class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        M, N = len(word1), len(word2)
        i, j = 0, 0

        while i < M and j < N:
            if i == j:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
        
        while i < M:
            ans.append(word1[i])
            i += 1
        while j < N:
            ans.append(word2[j])
            j += 1
        
        return "".join(ans)