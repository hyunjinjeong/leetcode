class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # 나 dp요 하고 있는 문제인데..
        # i번째를 사용하려면 이전 dp에서 조건을 만족하는 character 중 최댓값을 구해야 함..
        # 그러면 hashmap으로 index를 저장해둘까?
        def get_candidates(c):
            for num in range(ord(c) - k, ord(c) + k + 1):
                yield chr(num)
        
        dp = [1] * len(s)
        index_map = {}

        for i, c in enumerate(s):
            for candidate in get_candidates(c):
                if candidate in index_map:
                    dp[i] = max(dp[i], dp[index_map[candidate]] + 1)

            index_map[c] = i
        
        return max(dp)
            