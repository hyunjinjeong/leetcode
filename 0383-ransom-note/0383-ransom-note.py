class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = collections.Counter(ransomNote)
        magazine_counter = collections.Counter(magazine)
        
        for key in ransom_counter:
            if key not in magazine_counter:
                return False
            if magazine_counter[key] < ransom_counter[key]:
                return False
        
        return True