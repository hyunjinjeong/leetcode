class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # subarray마다 길이가 k개까지 갈 수 있는데...
        # 그냥 모든 경우의 수를 다 생성하는 건가?
        # 그 subarray의 합은 최댓값 * 길이가 될거고..
        
        @cache
        def dfs(start):
            if start == len(arr):
                return 0
            
            res = 0 
            for i in range(start, min(start + k, len(arr))):
                max_value = max(arr[start:i + 1])
                size = i - start + 1
                res = max(res, (max_value * size) + dfs(i + 1))
            
            return res
        
        return dfs(0)