class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 0번쨰부터 n-1번째까지 그냥 돌아야 하나?
        # 0에서 시작한다고 하면
        # gas[0]으로 시작. gas[0] - cost[1] < 0 이면 못감
        # 그렇게 해서 + gas[1]. 해서 - cost[2] < 0인지 또 체크...
        # 이러면 O(n^2)인데
        # greedy하게 diff가 > 0 인지 체크하면 됐었음..
        
        # 답이 없는 경우
        if sum(gas) < sum(cost):
            return -1

        start, diff = 0, 0
        for i in range(len(gas)):
            diff += gas[i] - cost[i]
            if diff < 0:
                start = i + 1
                diff = 0

        return start