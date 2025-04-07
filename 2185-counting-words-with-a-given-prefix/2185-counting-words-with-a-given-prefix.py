class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if len(pref) > len(word):
                continue

            pref_index = 0
            for c in word:
                if c != pref[pref_index]:
                    break

                pref_index += 1
                if pref_index == len(pref):
                    break
            
            if pref_index == len(pref):
                res += 1
        
        return res