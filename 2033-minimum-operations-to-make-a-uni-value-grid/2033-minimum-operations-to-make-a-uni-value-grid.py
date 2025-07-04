class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 불가능한 조건은? 각 숫자간의 차이가 x의 배수가 아니면 불가능함.
        # 높은 수에서 x를 빼는건 낮은 수에서 x를 더하는 것과 같음
        # 흠 min ops를 어떻게 구할까
        # 이 문제에서는 2D는 아무 의미 없고
        # 가운데 있는 숫자를 골라야 할 듯. 정렬하기? 짝수개면 2개 중 min을 구하고..
        def get_ops(target_num):
            ops = 0
            for num in arr:
                ops += abs(target_num - num) // x
            return ops

        M, N = len(grid), len(grid[0])

        arr = [0] * (M * N)
        for i in range(M):
            for j in range(N):
                if abs(grid[i][j] - grid[0][0]) % x != 0:
                    return -1
                arr[i * N + j] = grid[i][j]
        
        arr.sort()

        if len(arr) % 2 == 1:
            mid_num = arr[len(arr) // 2]
            return get_ops(mid_num)
        else:
            mid_num1 = arr[len(arr) // 2 - 1]
            mid_num2 = arr[len(arr) // 2]
            return min(get_ops(mid_num1), get_ops(mid_num2))
