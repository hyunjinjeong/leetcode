class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l1, l2 = 0, 0
        r1, r2 = 0, 0

        while l1 < len(word1) or r1 < len(word2):
            if l1 == len(word1) and r1 < len(word2) or l1 < len(word1) and r1 == len(word2):
                return False

            if word1[l1][l2] != word2[r1][r2]:
                return False
            
            if l2 == len(word1[l1]) - 1:
                l1 += 1
                l2 = 0
            else:
                l2 += 1
            
            if r2 == len(word2[r1]) - 1:
                r1 += 1
                r2 = 0
            else:
                r2 += 1
        
        return True