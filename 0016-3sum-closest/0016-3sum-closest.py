class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for left in range(len(nums)):
            if left > 1 and nums[left] == nums[left-1]:
                continue
            
            mid, right = left + 1, len(nums) - 1
            while mid < right:
                current_sum = nums[left] + nums[mid] + nums[right]
                if current_sum == target:
                    ans = target
                    break
                
                if abs(current_sum - target) < abs(ans - target):
                    ans = current_sum
                
                if current_sum < target:
                    mid += 1
                else:
                    right -= 1
            
        return ans