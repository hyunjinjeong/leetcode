class Solution:
    def longestPalindrome(self, s):
        # dp를 dp[i][j]는 s[i:j+1]이 palindrome인 경우로 정의하고..
        # array를 시작과 끝으로 돌면서 이전 결과를 활용하면 된다.
        dp = [[False] * len(s) for _ in range(len(s))]
        
        # 길이 1짜리 초기화
        for i in range(len(s)):
            dp[i][i] = True
        
        pos = (0, 1)
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    continue
                
                # 처음과 끝이 같은 경우...
                # j-i == 1이면 길이가 2인 경우. 엣지 케이스.
                if j-i == 1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    
                    if pos[1] - pos[0] < j+1-i:
                        pos = (i, j+1)
        
        return s[pos[0]:pos[1]]
                    
            