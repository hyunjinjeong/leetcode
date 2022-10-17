class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_s = ""
        for c in s:
            if c.isalnum():
                refined_s += c.lower()
        
        return refined_s == refined_s[::-1]