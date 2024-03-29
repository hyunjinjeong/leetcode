class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # in-place로 nums에서 val을 제거하고, len(nums)를 리턴하는 거네
        
        # # swap + pop해서 O(1)로 처리하자        
        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         nums[i], nums[-1] = nums[-1], nums[i]
        #         nums.pop()
        #     else:
        #         i += 1

        # 실제로 삭제할 필요는 없넹
        # 앞에서 k번째까지만 val이 아닌 아이템으로 채워두면 됨
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        
        return i
