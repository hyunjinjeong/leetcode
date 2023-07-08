class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 딱봐도 binary search인데...
        # mid를 matrix[r][c]로 치환할 수 있을까?
        # matrix[mid // C][mid % C] 요건가?
        M, N = len(matrix), len(matrix[0])

        left, right = 0, M * N - 1
        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // N][mid % N]
            if target == num:
                return True
            
            if target < num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
