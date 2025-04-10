class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # brute force는 2중 for문
        # 최적화하려면..? 
        # 전체 pair 개수는 N-1 + N-2 + ... 1 == N * (N - 1) // 2
        # good pair는 j - i == nums[j] - nums[i] -> nums[i] - i == nums[j] - j
        # 그럼 저 nums[i] - i의 count를 저장해두면 될 듯?
        N = len(nums)
        res = N * (N - 1) // 2

        diff_count = collections.defaultdict(int)
        for i, num in enumerate(nums):
            res -= diff_count[num - i]
            diff_count[num - i] += 1
        return res