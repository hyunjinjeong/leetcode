class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. O(n) 공간 쓰는건 쉬움
        counter = collections.defaultdict(int)
        
        for num in nums:
            counter[num] += 1
            if counter[num] > len(nums) // 2:
                return num