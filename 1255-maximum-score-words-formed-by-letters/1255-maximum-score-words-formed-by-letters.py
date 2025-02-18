class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # dp 같은디. pick & not pick?
        # backtracking이구만
        def get_score(word):
            res = 0
            for c in word:
                res += score[ord(c) - ord("a")]
            return res
        
        def is_valid_word(word_letter_count):
            for c in word_letter_count:
                if word_letter_count[c] > letters_count[c]:
                    return False
            return True        

        def dfs(i):
            if i == len(words):
                return 0

            # not pick
            res = dfs(i + 1)
            
            # pick
            word_letter_count = collections.Counter(words[i])
            if is_valid_word(word_letter_count):
                for c in word_letter_count:
                    letters_count[c] -= word_letter_count[c]
                
                res = max(get_score(words[i]) + dfs(i + 1), res)
                
                for c in word_letter_count:
                    letters_count[c] += word_letter_count[c]
            
            return res

        letters_count = collections.Counter(letters)
        return dfs(0)