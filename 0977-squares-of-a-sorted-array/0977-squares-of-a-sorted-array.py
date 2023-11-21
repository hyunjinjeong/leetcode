class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(n)을 생각해보자.
        # 투 포인터? 음수, 양수 각각 나눠서
        # 하나씩 비교해가면서 하면 되지 않을까...
        
        # 1. 전부 양수인 경우
        if nums[0] >= 0:
            return [num ** 2 for num in nums]
        
        # 2. 전부 음수인 경우:
        if nums[-1] <= 0:
            return [num ** 2 for num in sorted(nums, reverse=True)]
            
        # 3. 일반적인 경우
        l, r = 0, 0
        for i, num in enumerate(nums):
            if num >= 0:
                l, r = i - 1, i
                break
        
        # 투 포인터 돌기
        ans = []
        while l >= 0 and r < len(nums):
            left, right = nums[l], nums[r]
            if abs(left) >= abs(right):
                ans.append(right ** 2)
                r += 1
            else:
                ans.append(left ** 2)
                l -= 1
        
        # 남은거 마저 돌기
        while l >= 0:
            ans.append(nums[l] ** 2)
            l -= 1
        while r < len(nums):
            ans.append(nums[r] ** 2)
            r += 1
        
        return ans