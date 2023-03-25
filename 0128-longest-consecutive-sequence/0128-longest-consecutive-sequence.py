class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         # 1. 일단 set 활용한 거
#         s, ans = set(nums), 0
        
#         for num in s:
#             # 여기서 -1 체크하는 이유는 +1 ...로 검사하기 때문에.
#             if num - 1 in s:
#                 continue
            
#             j = 1
#             while num + j in s:
#                 j += 1
            
#             ans = max(ans, j)
        
#         return ans
        
        # 2. Union-Find 활용.
        # Union-Find 함수 정의
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parents[root_b] = root_a
                size[root_a] += size[root_b]
        
        if not nums:
            return 0
        
        num_set = set(nums)
        
        # disjoint set 초기화
        parents, size = {}, {}
        for num in num_set:
            parents[num] = num
            size[num] = 1
        
        # Union
        for num in num_set:
            if num - 1 in num_set:
                union(num, num-1)
            if num + 1 in num_set:
                union(num, num+1)
        
        return max(size.values())