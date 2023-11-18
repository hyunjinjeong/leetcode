class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for i in range(len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        # prefix_sum[right] - prefix_sum[left - 1]
        # 그러면 prefix_sum에 dummy를 하나 둬야겠다. right + 1, left가 될거고.
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)