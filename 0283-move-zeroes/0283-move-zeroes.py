class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         # 1. 요게 젤 간단한 버전.
#         zero_count = 0
#         for num in nums:
#             if num == 0:
#                 zero_count += 1
        
#         tmp = []
#         for num in nums:
#             if num != 0:
#                 tmp.append(num)
        
#         for _ in range(zero_count):
#             tmp.append(0)
        
#         i = 0
#         while i < len(nums):
#             nums[i] = tmp[i]
#             i += 1
        
#         # 2. 간단하게
#         pos_last_non_zero = 0
        
#         # 일단 0이 아닌 애들을 미리 앞으로 땡겨준다. 
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[pos_last_non_zero] = nums[i]
#                 pos_last_non_zero += 1
        
#         # non-zero는 이미 앞에 다 와있음. 나머지는 0으로 채워준다.
#         for i in range(pos_last_non_zero, len(nums)):
#             nums[i] = 0
        
        # # 3. two-pointer 사용하는 방법도 있다..ㄷㄷ
        # slow = 0
        # # 이러면 모든 non-zero가 앞으로 오고, 0은 다 뒤로 가게 됨.
        # for fast in range(len(nums)):
        #     if nums[fast] != 0:
        #         nums[fast], nums[slow] = nums[slow], nums[fast]
        #         slow += 1
        
        # 4. 3번에서 operation 수를 줄인 버전.
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            
            if nums[slow] != 0:
                slow += 1