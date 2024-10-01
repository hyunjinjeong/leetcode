class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # 나 dp요 하고 있는 문제인데..
        # i번째를 사용하려면 이전 dp에서 조건을 만족하는 character 중 최댓값을 구해야 함..
        # 그러면 hashmap으로 index를 저장해둘까?
        # dp를 줄일 수 있구나
        dp = [0] * 26

        for i, c in enumerate(s):
            index = ord(c) - ord("a")

            best = 0
            for prev in range(max(0, index - k), min(26, index + k + 1)):
                best = max(best, dp[prev])
            
            dp[index] = best + 1
        
        return max(dp)
            