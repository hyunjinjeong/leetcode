class Solution:
    def clearDigits(self, s: str) -> str:
        non_digits = []
        for c in s:
            if c.isdigit():
                if non_digits:
                    non_digits.pop()
            else:
                non_digits.append(c)
        
        return "".join(non_digits)