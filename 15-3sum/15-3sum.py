class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        
        nums.sort()
        
        for left in range(len(nums)):
            # 하나를 고르고 나서.. 그 다음에 two-sum 적용하면 된다!
            # 중복은 매번 체크하면 TLE가 떠서 정렬 후 투 포인터 사용...
            if left > 1 and nums[left] == nums[left-1]:
                continue
            
            target = 0 - nums[left]
            mid, right = left + 1, len(nums) - 1
            while mid < right:
                current_sum = nums[mid] + nums[right]
                if current_sum == target:
                    answer.add((nums[left], nums[mid], nums[right]))
                    mid += 1
                    right -= 1
                elif current_sum < target:
                    mid += 1
                else:
                    right -= 1
            
        return list(answer)