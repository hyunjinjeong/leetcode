class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mappings = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return self.backtrack(0, [], mappings, digits, [])
    
    def backtrack(self, index, curr, mappings, digits, ans):
        if index == len(digits):
            ans.append("".join(curr))
            return ans
        
        for letter in mappings[digits[index]]:
            curr.append(letter)
            self.backtrack(index + 1, curr, mappings, digits, ans)
            curr.pop()
        
        return ans
