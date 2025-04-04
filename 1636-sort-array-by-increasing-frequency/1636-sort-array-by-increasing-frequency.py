class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        arr = sorted(counter.items(), key=lambda tup: (tup[1], -tup[0]))
        
        res = []
        for num, count in arr:
            for _ in range(count):
                res.append(num)
        return res