class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # 뭔가 규칙이 있으려나
        # 인접한 셀을 옮겨다닐 수 있기 때문에 아무 2개의 셀을 뒤집을 수 있음
        # 그러면 음수가 짝수개 있으면 다 양수로 생각하면 되고, 홀수개 있으면 가장 절댓값이 낮은 숫자만 음수로 남겨두면 될 듯
        N = len(matrix)

        negative_count = 0
        total_sum = 0
        smallest_abs = float("inf")

        for i in range(N):
            for j in range(N):
                num = matrix[i][j]
                
                total_sum += abs(num)
                smallest_abs = min(abs(num), smallest_abs)
                
                if num < 0:
                    negative_count += 1

        if negative_count % 2 == 0:
            return total_sum
        else:
            return total_sum + smallest_abs * -2 # 1번은 양수로 더해져 있으므로
