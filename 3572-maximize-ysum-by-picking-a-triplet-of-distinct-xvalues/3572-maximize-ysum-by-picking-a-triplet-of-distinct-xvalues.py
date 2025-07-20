class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        # x[i]를 그룹으로 묶어서 y[i]가 가장 높은 아이템만 남기면 되지 않을까
        # 그러면 그냥 3개 뽑아서 max를 구하면 됨
        # 1 2 1 3 2 / 5 3 4 6 2 의 경우
        # 1 2 3 / 5 3 6
        N = len(x)

        group = {}
        for i in range(N):
            group[x[i]] = max(y[i], group.get(x[i], 0))
        
        if len(group) < 3:
            return -1

        return sum(sorted(group.values(), reverse=True)[:3])
