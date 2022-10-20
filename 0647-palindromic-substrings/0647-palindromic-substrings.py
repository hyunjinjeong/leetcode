class Solution:
    def countSubstrings(self, s: str) -> int:
        # 아까 문제랑 같은거 아닌가?
        # dp로 palindrome이면 True로 해서 True의 갯수를 세면 될 것 같은데
        
        dp = [[False] * len(s) for _ in range(len(s))]
        answer = 0
        
        # 길이 1짜리 초기화
        for i in range(len(s)):
            dp[i][i] = True
            answer += 1
            
        for end in range(len(s)):
            for start in range(end-1, -1, -1):
                if s[start] != s[end]:
                    continue
                
                # 시작과 끝이 같은 경우.
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    answer += 1
        
        return answer