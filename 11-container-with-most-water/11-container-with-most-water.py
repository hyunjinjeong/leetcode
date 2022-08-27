class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = -1
        
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(current_area, max_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        
        
        
    