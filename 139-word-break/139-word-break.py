class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1) # dp[i]는 s[:i+1]이 wordDict로 구성되는지.
        dp[0] = True # 코너 케이스
        
        for i in range(len(s)):
            if not dp[i]:
                continue
                
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    dp[j+1] = True
        
        return dp[-1]
                