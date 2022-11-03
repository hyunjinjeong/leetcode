class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         # 1. 요건 time: O(nlogn), 공간: O(n) 임.
#         sorted_nums = sorted(nums)
        
#         answer, answer_count = 0, 0
#         curr_count = 0
#         i = 0
#         while i < len(sorted_nums):
#             num = sorted_nums[i]
#             count = 0
#             j = i
#             while j < len(sorted_nums) and sorted_nums[i] == sorted_nums[j]:
#                 count += 1
#                 j += 1
            
#             if count > answer_count:
#                 answer, answer_count = num, count
            
#             i = j
            
#         return answer

        # # 2. 근데 답을 보니 가장 많이 나온게 2/n보다 많다는 걸 이용해서 걍 인덱스로 찾을 수 있네 ㅋㅋ
        # sorted_nums = sorted(nums)
        # return sorted_nums[len(nums)//2]

        
        # 3. follow-up으로 시간: O(n), 공간: O(1)로...
        # Boyer-Moore 알고리즘 사용하면 된다.
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate