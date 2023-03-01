class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1) # dp[n]은 s[0:n]이 wordDict로 구성되는지.
        dp[0] = True # 코너 케이스
        
        for left in range(len(s)):
            if not dp[left]:
                continue
                
            for right in range(left, len(s)):
                word = s[left:right+1]
                if word in wordDict:
                    dp[right+1] = True
        
        return dp[-1]