class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        @cache
        def dfs(i, j):
            if j == len(key):
                return 0
            
            res = float("inf")
            for ring_index in range(len(ring)):
                if ring[ring_index] != key[j]:
                    continue
                
                min_dist = min(abs(ring_index - i), len(ring) - abs(ring_index - i))
                res = min(res, min_dist + 1 + dfs(ring_index, j + 1))
            
            return res
        
        return dfs(0, 0)