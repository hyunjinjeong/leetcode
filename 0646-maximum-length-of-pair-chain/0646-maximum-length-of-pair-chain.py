class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 정렬을 left로 할지 right로 할지..
        # 14 23 56 이렇게 있다고 치면
        # right로 정렬하면 23 14 56
        # right로 정렬하는게 더 쉬워 보이네
        # 그리고 curr[0] prev[1] 비교하고..
        # longest chain이면 dp같은걸 사용해야 하려나..?
        # 근데 이전 chain의 max는 어떻게 찾지? 1~left까지 찾으면 되나.. 최대 1000개니까 가능할 듯
        N = len(pairs)
        pairs.sort(key=lambda p: p[1])

        dp = [1] * N

        for i in range(N):
            left, right = pairs[i]
            prev_max = 0
            for j in range(i):
                if pairs[j][1] < left:
                    prev_max = max(prev_max, dp[j])
            dp[i] = prev_max + 1

        return max(dp)