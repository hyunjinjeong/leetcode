class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # 최소 wage[i]만큼 줘야 하고, quality[i]에 비례해서 줘야 함. 요렇게 k명을 고용했을 때 min cost
        # q[i] / w[i]가 모든 i에 대해서 동일해야 함.
        N = len(quality)
        res = float("inf")

        wage_to_quality_ratio = [(wage[i] / quality[i], i) for i in range(N)]
        wage_to_quality_ratio.sort(key=lambda k: k[0])

        workers = []
        curr_total_quality = 0
        for ratio, i in wage_to_quality_ratio:
            curr_total_quality += quality[i]
            heapq.heappush(workers, -quality[i])

            if len(workers) > k:
                curr_total_quality += heapq.heappop(workers)
            
            if len(workers) == k:
                res = min(curr_total_quality * ratio, res)
        
        return res