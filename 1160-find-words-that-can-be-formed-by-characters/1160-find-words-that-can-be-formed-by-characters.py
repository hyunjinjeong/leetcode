class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        
        dt = {}
        for c in chars:
            dt[c] = dt.get(c, 0) + 1
            
        for word in words:
            word_dt = {}
            is_good = True
            for c in word:
                if c not in dt:
                    is_good = False
                    break
                word_dt[c] = word_dt.get(c, 0) + 1
                if word_dt[c] > dt[c]:
                    is_good = False
                    break

            if is_good:
                ans += len(word)
        
        return ans
        