class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mappings = { "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        return self.backtrack(0, [], mappings, digits, [])
    
    def backtrack(self, index, curr, mappings, digits, ans):
        if index == len(digits):
            ans.append("".join(curr))
            return ans
        
        for c in mappings[digits[index]]:
            curr.append(c)
            self.backtrack(index + 1, curr, mappings, digits, ans)
            curr.pop()
        
        return ans
