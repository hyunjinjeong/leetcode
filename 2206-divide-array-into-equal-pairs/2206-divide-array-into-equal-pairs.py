class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # count를 세면 될 듯
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        for count in counter.values():
            if count % 2 == 1:
                return False
        
        return True