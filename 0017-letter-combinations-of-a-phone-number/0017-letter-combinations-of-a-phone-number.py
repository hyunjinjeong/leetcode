class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dt = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        result = []
        
        def dfs(index, current):
            if index == len(digits):
                result.append(current)
                return
            
            letters = dt[digits[index]]
            for letter in letters:
                dfs(index + 1, current + letter)
            
        dfs(0, "")
        return result
