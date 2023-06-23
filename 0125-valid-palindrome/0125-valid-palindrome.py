class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined = []

        for c in s:
            if not c.isalnum():
                continue
            refined.append(c.lower())
        
        ans = True

        left, right = 0, len(refined) - 1
        while left < right:
            if refined[left] != refined[right]:
                ans = False
                break
            
            left += 1
            right -= 1

        return ans