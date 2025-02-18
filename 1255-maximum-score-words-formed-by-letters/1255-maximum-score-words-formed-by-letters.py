class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # dp 같은디. pick & not pick?
        def get_score(c):
            return score[ord(c) - ord("a")]
        
        def get_score_word(word):
            res = 0
            for c in word:
                res += get_score(c)
            return res

        letters_count = collections.Counter(letters)

        def dfs(i, letters_count):
            if i == len(words):
                return 0
            
            can_pick = True
            
            word_letter_count = collections.Counter(words[i])
            for c in word_letter_count:
                if word_letter_count[c] > letters_count[c]:
                    can_pick = False
                    break
            
            # pick
            if can_pick:
                for c in word_letter_count:
                    letters_count[c] -= word_letter_count[c]
                pick = get_score_word(words[i]) + dfs(i + 1, letters_count)
                for c in word_letter_count:
                    letters_count[c] += word_letter_count[c]
            else:
                pick = 0
            
            # not pick
            not_pick = dfs(i + 1, letters_count)

            return max(pick, not_pick)

        return dfs(0, letters_count)