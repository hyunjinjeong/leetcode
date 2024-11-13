class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)

        # it seems like backtracking
        def backtrack(start, curr):
            if start == len(s):
                self.res.append(" ".join(curr))
                return
            
            for i in range(start, len(s)):
                word = s[start:i + 1]
                if word in word_set:
                    curr.append(word)
                    backtrack(i + 1, curr)
                    curr.pop()

        self.res = []
        backtrack(0, [])
        return self.res