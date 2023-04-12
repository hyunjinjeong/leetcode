class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 딱봐도 binary search인데...
        # 길이가 12면 mid가 6일 때
        # mid를 matrix[r][c]로 치환할 수 있을까?
        # matrix[mid // C][mid % C] 요건가?
        
        R, C = len(matrix), len(matrix[0])
        left, right = 0, R*C
        
        while left < right:
            mid = (left + right) // 2
            item = matrix[mid // C][mid % C]
            
            if item == target:
                return True
            
            if item < target:
                left = mid + 1
            else:
                right = mid
        
        return False
            