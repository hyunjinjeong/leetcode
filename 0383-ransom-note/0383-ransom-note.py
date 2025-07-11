class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = collections.Counter(magazine)

        for c in ransomNote:
            if c not in magazine_count or magazine_count[c] == 0:
                return False
            
            magazine_count[c] -= 1
        
        return True
