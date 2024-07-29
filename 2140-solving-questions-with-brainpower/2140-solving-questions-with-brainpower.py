class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # 너무 대놓고 dp
        # i번째를 포함하느냐, 포함하지 않느냐.. 로 가야 하나?
        N = len(questions)

        # 뒤에서부터 돌아야 할 듯. 앞에서부터 돌면 i번째 이전에 뭐가 있는지 찾을 수가 없다
        # 그러면 dp 배열에는 max를 저장하면 되려나?

        dp = [0] * N
        dp[N-1] = questions[N-1][0]
        
        for i in range(N - 2, -1, -1):
            points, brainpower = questions[i]
            # i + brainpower가 N보다 클 수도 있으니까...
            if i + brainpower + 1 < N:
                dp[i] = max(dp[i+1], points + dp[i + brainpower + 1])
            else:
                dp[i] = max(dp[i+1], points)
        
        return dp[0]