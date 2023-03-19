class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ?? 투포인터는 머지
        # https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        # 이 알고리즘을 기반으로 하고 있다고 한다.
        
        # 1. Find longest non-increasing suffix
        suffix = len(nums) - 1
        while suffix > 0 and nums[suffix-1] >= nums[suffix]:
            suffix -= 1
        
        # 이러면 전체가 거꾸로 뒤집어진 것. 즉 마지막 시퀀스이므로 처음으로 돌리면 됨
        if suffix == 0:
            nums.reverse()
            return
        
        # 2. Identify pivot: 1번에서 찾은 index-1
        pivot = suffix - 1
        
        # 3. Find rightmost successor to pivot in the suffix
        successor = len(nums) - 1
        while nums[successor] <= nums[pivot]:
            successor -= 1
        
        # 4. Swap with pivot
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        
        # 5. Reverse the suffix
        left, right = suffix, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1