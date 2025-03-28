class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # 최대한 반씩 자르는게 좋을 것 같은데
        # 근데 3~4가 있으면 뭘 고르지??
        # brute force로 하려면 경우의 수 len(cuts)!
        # len(cuts)는 최대 100이긴 하다
        # DP..?
        @cache
        def dfs(start, end):
            if end - start == 1:
                return 0
            
            res = float("inf")
            for cut in cuts:
                if cut <= start or cut >= end:
                    continue
                
                res = min(end - start + dfs(start, cut) + dfs(cut, end), res)
            
            return res if res < float("inf") else 0
        
        return dfs(0, n)