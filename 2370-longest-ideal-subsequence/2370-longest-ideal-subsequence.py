class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # 나 dp요 하고 있는 문제인데..
        # i번째를 사용하려면 이전 dp에서 조건을 만족하는 character 중 최댓값을 구해야 함..
        # 그러면 hashmap으로 index를 저장해둘까?
        
        def diff(a, b):
            return abs(ord(a) - ord(b))
        
        dp = [1] * len(s)
        index_map = {}

        for i in range(len(s)):
            # k가 있으면.. -k ~ k까지 범위의 character를 모두 확인해봐야 함
            # 일단 간단하게 그냥 모든 케이스를 확인해보자..
            for c in "abcdefghijklmnopqrstuvwxyz":
                if diff(s[i], c) <= k and c in index_map:
                    dp[i] = max(dp[i], dp[index_map[c]] + 1)

            index_map[s[i]] = i
        
        return max(dp)
            