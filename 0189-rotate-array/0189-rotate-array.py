class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # 각각 뒤집고, 합쳐서 뒤집고
        # 4 3 2 1 / 7 6 5
        # 5 6 7 1 2 3 4
        
        k = k % N # nums보다 크면 의미가 없으니
        
        reverse(0, N - k - 1)
        reverse(N - k, N - 1)
        reverse(0, N - 1)
        
        