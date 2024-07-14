class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 절반은 A도시로, 나머지 절반은 B도시로. 이 때 min을 구해야 함
        # A-B difference를 생각하기?
        # 394, 259, 45, 722, 88. 즉 A로 가면 그만큼 합이 늘어난다는 거임
        # 여기서 작은거 2개를 넣으면..? 일단 답이 맞다.
        
        # 1. 일단 작은 값을 먼저 넣어보기
        ans = 0
        a_set, b_set = set(), set()
        for i, (a_cost, b_cost) in enumerate(costs):
            if a_cost < b_cost:
                a_set.add(i)
                ans += a_cost
            else:
                b_set.add(i)
                ans += b_cost
        
        count_diff = len(a_set) - len(b_set)
        print(count_diff)
        if count_diff == 0:
            return ans
        
        # a가 더 많은 경우. a에 들어있는 친구들은 모두 b_cost >= a_cost라서 들어온거임
        heap = []
        if count_diff > 0:
            for i in a_set:
                a_cost, b_cost = costs[i]
                heap.append(b_cost - a_cost)
        else: # 반대로 b가 많은 경우
            count_diff *= -1
            for i in b_set:
                a_cost, b_cost = costs[i]
                heap.append(a_cost - b_cost)
        heapq.heapify(heap)

        # a a a a b b b b

        while count_diff:
            additional_cost = heapq.heappop(heap)
            ans += additional_cost

            count_diff -= 2
        
        return ans