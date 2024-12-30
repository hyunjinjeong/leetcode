class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # ages 순으로 정렬해서 monotonic stack에 쌓으면 될 것 같은데..가 아니고 같은 age면 score가 높아도 되는구나
        # pick & not pick DP인가?

        # 나이로 정렬은 해야할 듯
        ages_and_scores = sorted([(age, score) for age, score in zip(ages, scores)], key=lambda pair: (pair[0], pair[1]))

        N = len(scores)
        dp = [0] * N

        for i in range(N):
            dp[i] = ages_and_scores[i][1]
            for j in range(i):
                if ages_and_scores[j][1] <= ages_and_scores[i][1]:
                    dp[i] = max(dp[j] + ages_and_scores[i][1], dp[i])
        
        return max(dp)