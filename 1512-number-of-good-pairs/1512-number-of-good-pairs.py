class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 같은 수가 n개 있으면 nc2 아닌가?
        counter = collections.Counter(nums)

        ans = 0
        for num in counter:
            if counter[num] >= 2:
                ans += counter[num] * (counter[num] - 1) // 2
        
        return ans