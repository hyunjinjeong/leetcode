class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        word_dict_set = set(wordDict)

        dp = [False] * (N + 1)
        dp[0] = True

        for end in range(N + 1):
            for word in wordDict:
                word_len = len(word)
                start = end - word_len
                if start < 0:
                    continue
                if not dp[start]:
                    continue
                
                sub_str = s[start:end]
                if sub_str in word_dict_set:
                    dp[end] = True
                    break

        return dp[N]