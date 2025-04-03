class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        
        res = 0
        for word in words:
            is_valid = True
            for c in word:
                if c not in allowed_set:
                    is_valid = False
                    break

            if is_valid:
                res += 1
        
        return res
