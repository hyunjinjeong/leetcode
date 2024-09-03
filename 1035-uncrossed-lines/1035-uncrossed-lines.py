class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 규칙을 생각해보자
        # 일단 nums1 - nums2를 이었을 때... 
        # index를 각각 i, j라고 하면 그 사이 범위의 인덱스 (inclusive)는 연결할 수가 없음
        # 즉 ~i-1, j+1~ 범위로 다시 연결 가능...
        # LCS랑 똑같은 문제였다!
        cache = {}

        def dfs(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if nums1[i] == nums2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                res = max(dfs(i, j + 1), dfs(i + 1, j))
            
            cache[(i, j)] = res
            return res
        
        return dfs(0, 0)
        