class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
#         # top-down DP로 잘 했었넹.. 근데 이전 계산을 계속 반복해서 lru_cache가 필요했음.
#         @lru_cache(None)
#         def rec(curr_index):
#             # 빠져나갈 곳들.
#             if curr_index > len(nums) - 1:
#                 return False
#             if curr_index == len(nums) - 1:
#                 return True
            
#             for jump_length in range(nums[curr_index], 0, -1):
#                 if rec(curr_index + jump_length):
#                     return True
            
#             return False
            
#         return rec(0)
    
        # Optimal solution. Greedy. 시간 O(n) 공간 O(1)
        last_position = len(nums) - 1
        # 뒤에서부터 시작해서 last_position을 업데이트
        # 현재 인덱스 + jump length가 last_position 보다 크면 결국 최종까지 도달 가능해짐...
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        
        # last_position이 시작점(0)까지 업뎃 되었는가.
        return last_position == 0