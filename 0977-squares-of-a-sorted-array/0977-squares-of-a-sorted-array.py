class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(n) 쏠루션을 찾아봅시다
        
        square_nums = [num ** 2 for num in nums]
        square_nums.sort()
        return square_nums
