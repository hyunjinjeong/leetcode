class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        self.helper(digits, "", result)
        return result

    def helper(self, digits, s, result):
        if not digits:
            result.append(s)
            return
        
        chars = self.get_chars(digits[0])
        for c in chars:
            self.helper(digits[1:], s+c, result)
        
    def get_chars(self, n):
        num = int(n)
        s = "abcdefghijklmnopqrstuvwxyz"
        
        if num <= 6:
            return s[(num-2)*3:(num-2)*3+3]
        if num == 7:
            return "pqrs"
        if num == 8:
            return "tuv"
        if num == 9:
            return "wxyz"
        
            