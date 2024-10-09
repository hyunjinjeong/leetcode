class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # 흠.. O(1) 메모리는 걍 불가능한 거였음. 뭐지;
        neg, pos = [], []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = pos[i // 2]
            else:
                nums[i] = neg[i // 2]

        return nums