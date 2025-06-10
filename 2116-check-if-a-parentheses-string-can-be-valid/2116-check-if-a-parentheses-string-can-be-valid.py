class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        max_open_parenthesis, min_open_parenthesis = 0, 0
        for i in range(len(s)):
            if locked[i] == "0":
                max_open_parenthesis += 1 # "("
                min_open_parenthesis -= 1 # ")"
            else:
                if s[i] == "(":
                    max_open_parenthesis += 1
                    min_open_parenthesis += 1
                else:
                    max_open_parenthesis -= 1
                    min_open_parenthesis -= 1

            if max_open_parenthesis < 0:
                return False
            
            min_open_parenthesis = max(min_open_parenthesis, 0)
        
        return min_open_parenthesis == 0
