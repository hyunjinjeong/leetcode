class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         # 1. 이건 counting sort 느낌으로... 대신 2-pass임
#         counts = [0, 0, 0]
#         for num in nums:
#             counts[num] += 1
        
#         for i in range(1, 3):
#             counts[i] += counts[i-1]
        
#         prev_index = 0
#         for i in range(3):
#             count = counts[i]
#             for j in range(prev_index, count):
#                 nums[j] = i
#             prev_index = count
        
        # 이건 2-pointer 변형한 3-pointer. 0을 모두 왼쪽 2를 모두 오른쪽으로 몰아버리는 아이디어.
        # https://leetcode.com/problems/sort-colors/discuss/681526/Python-O(n)-3-pointers-in-place-approach-explained
        zero, one, two = 0, 0, len(nums) - 1
        
        while one <= two:
            if nums[one] == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1