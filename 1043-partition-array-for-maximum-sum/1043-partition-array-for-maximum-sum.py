class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # subarray마다 길이가 k개까지 갈 수 있는데...
        # 그냥 모든 경우의 수를 다 생성하는 건가?
        # 그 subarray의 합은 최댓값 * 길이가 될거고..
        # 그러면 DP로 풀 수 있겠다
        N = len(arr)
        dp = [0] * (N + 1)

        for i in range(N - 1, -1, -1):
            max_value = 0
            for j in range(i, min(i + k, len(arr))):
                max_value = max(max_value, arr[j])
                dp[i] = max(dp[i], dp[j + 1] + max_value * (j - i + 1))

        return dp[0]