class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 그냥 counter 만들어서 하면 되는데.. 그건 easy고
        # O(N) time, O(1) space에 하는게 medium인가
        total_count = len(nums)
        counter = collections.defaultdict(int)

        res = []
        for num in nums:
            counter[num] += 1
            if counter[num] == total_count // 3 + 1:
                res.append(num)
        
        return res
