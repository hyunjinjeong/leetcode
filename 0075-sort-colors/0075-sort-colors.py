class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED, WHITE, BLUE = 0, 1, 2
        # 2-pass는 쉽다. 그냥 각각 숫자 세서 그만큼 채워넣으면 됨..
        dt = collections.defaultdict(int)
        for num in nums:
            if num == RED:
                dt[RED] += 1
            elif num == WHITE:
                dt[WHITE] += 1
            else:
                dt[BLUE] += 1
        
        i = 0
        for _ in range(dt[RED]):
            nums[i] = RED
            i += 1
        for _ in range(dt[WHITE]):
            nums[i] = WHITE
            i += 1
        for _ in range(dt[BLUE]):
            nums[i] = BLUE
            i += 1
        