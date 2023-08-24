class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.backtrack(0, [], s, [])
    
    def backtrack(self, start, curr, s, ans):
        if start >= len(s):
            ans.append(curr[:])
            return ans
        
        for i in range(start, len(s)):
            sub_str = s[start:i+1]
            if self.is_palindrome(sub_str):
                curr.append(sub_str)
                self.backtrack(i + 1, curr, s, ans)
                curr.pop()
        
        return ans

    def is_palindrome(self, s):
        return s == s[::-1]