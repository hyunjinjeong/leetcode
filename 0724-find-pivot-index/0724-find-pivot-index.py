class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 왼쪽 오른쪽 각각 prefix sum 만들어두고 비교하면 되지 않을까
        left_sum, right_sum = [0], [0]

        for num in nums + [0]:
            left_sum.append(left_sum[-1] + num)
        for num in nums[::-1] + [0]:
            right_sum.append(right_sum[-1] + num)
        right_sum.reverse()

        for i in range(1, len(nums)+1):
            left, right = left_sum[i-1], right_sum[i+1]
            if left == right:
                return i - 1
        
        return -1