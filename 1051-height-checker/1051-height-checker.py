class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        res = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                res += 1
        return res