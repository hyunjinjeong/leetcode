class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         # 그래프로 풀어야 하는데 hash table 구현이 더 쉬워 보인다.
#         longest_streak = 0
        
#         num_set = set(nums)
        
#         # 여기 nums 쓸때랑 num_set 쓸 때랑 시간 차이가 엄청 나는데.. set에서 iterate 하는게 더 빠른가?
#         # 아 문제 조건 중에 모든 값이 고유하다는 조건이 없구나. 중복값이 있어서 그렇구만
#         for num in num_set:
#             # 요 if문 없으면 TLE 걸림. 1 2 3 4 5 6 7 ... 이런 케이스 생각해보면 된다
#             if num - 1 in num_set:
#                 continue
            
#             current_num = num
#             current_streak = 1
            
#             while current_num + 1 in num_set:
#                 current_num += 1
#                 current_streak += 1
            
#             longest_streak = max(longest_streak, current_streak)
        
#         return longest_streak
        
        # 그래프로 풀기... Union-Find 이용
        if not nums:
            return 0
        
        num_set = set(nums)
        
        # 자료구조 정의해서 쓰는 대신에 dict 사용해서 각각 관리
        group, size = {}, {}
        
        # disjoint set 초기화
        for num in num_set:
            group[num] = num
            size[num] = 1
        
        # Union-Find 함수 정의
        def find(a):
            if group[a] != a:
                group[a] = find(group[a])
            return group[a]
        
        def union(a, b):
            r_a, r_b = find(a), find(b)
            if r_a != r_b:
                group[r_b] = r_a
                size[r_a] += size[r_b]
        
        for num in num_set:
            if num - 1 in num_set:
                union(num, num-1)
            if num + 1 in num_set:
                union(num, num+1)
        
        return max(size.values())