class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        return sorted(nums, key=lambda num: (counter[num], -num))
