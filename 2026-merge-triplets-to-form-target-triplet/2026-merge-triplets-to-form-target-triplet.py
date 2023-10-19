class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 각각 최대를 찾으면 안됨..
        # 그럼 중간중간 단계에서 최댓값을 구해서 사용해야 하는데
        # 어떻게 돌려야 중간 최댓값이 정답인지 알 수 있을까
        # 답이 될 수 없는 것들 (target보다 큰 원소를 가진)을 제외하면 됨.

        ans = [0, 0, 0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                ans = [max(ans[0], t[0]), max(ans[1], t[1]), max(ans[2], t[2])]
        
        return ans == target